from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from bot.misc.jokes import get_random_joke
from infrastructure.database.models.users import User
from infrastructure.database.repo.requests import RequestsRepo

base_router = Router()


@base_router.message(CommandStart())
async def cmd_start(message: types.Message, user: User, session: AsyncSession, repo: RequestsRepo):
    print(user)
    random_joke = get_random_joke()
    welcome_message = (
        f"Привет, {message.from_user.first_name}!\nЯ SteamDuel, твой дуэльный секундант Steam-профилей.\n"
        f"Готов посмотреть, кто из вас выиграет в дуэли задротов? Давай проверим!\n"
        f"А еще у меня есть шутки про геймеров (/joke). Например: {random_joke}"
    )
    setting_message = (
        f"Чтобы я мог помочь тебе с дуэлями, мне нужна ссылка на твой Steam профиль.\n"
        f"Пожалуйста, отправь мне её, чтобы мы могли начать!"
    )
    await message.answer(welcome_message)
    await message.answer(setting_message)


@base_router.message(Command('help'))
async def help_command(message: types.Message):
    help_message = """
    Нужна помощь? Вот список доступных команд:
    1. /start - Зарегистрируй свой аккаунт, чтобы начать использовать бота.
    2. /help - Получи список всех команд, которые я поддерживаю.
    3. /menu - Открой меню, чтобы увидеть все мои функции.
    4. /joke - Послушай забавную шутку про геймеров.
    Если у тебя возникнут вопросы, я всегда готов помочь!
    """
    await message.answer(help_message)


@base_router.message(Command('menu'))
async def menu_command(message: types.Message):
    await message.answer("Меню готово!\nТеперь выбор за тобой - будто в RPG, только без драконов! 🐉")


@base_router.message(Command('joke'))
async def joke(message: types.Message):
    reply_text = get_random_joke()
    await message.reply(reply_text)
