from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def go_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.answer("Going on!")
