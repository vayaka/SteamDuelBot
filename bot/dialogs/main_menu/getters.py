from aiogram_dialog import DialogManager

from bot.misc.jokes import get_random_joke


async def get_joke(**kwargs):
    joke = get_random_joke()
    return {
        "joke": joke,
    }
