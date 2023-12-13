import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from bot.dialogs.main_menu.setup import bot_main_menu
from bot.middlewares.database import DatabaseMiddleware
from config import load_config, Config
from bot.handlers import routers_list
from bot.middlewares.config import ConfigMiddleware
from bot.services import broadcaster
from infrastructure.database.setup import create_engine, create_session_pool


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "The bot was launched!")


def register_global_middlewares(dp: Dispatcher, config: Config, session_pool=None):
    """
    Register global middlewares for the given dispatcher.
    Global middlewares here are the ones that are applied to all the handlers (you specify the type of update)

    :param dp: The dispatcher instance.
    :type dp: Dispatcher
    :param config: The configuration object from the loaded configuration.
    :param session_pool: Optional session pool object for the database using SQLAlchemy.
    :return: None
    """
    middleware_types = [
        ConfigMiddleware(config),
        DatabaseMiddleware(session_pool),
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging()

    config = load_config(".env")
    async_engine = create_engine(config.db, echo=False)
    session_pool = create_session_pool(async_engine)

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(*bot_main_menu())
    dp.include_routers(*routers_list)
    setup_dialogs(dp)

    register_global_middlewares(dp, config, session_pool=session_pool)

    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("The bot has been stopped!")
