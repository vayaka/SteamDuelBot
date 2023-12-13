from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager


async def on_link_entered(m: Message, widget: Any, manager: DialogManager, link: str):
    ctx = manager.current_context()
    print(link)
    await manager.next()
