from bot.handlers.base import base_router
from bot.handlers.user import user_router

routers_list = [
    base_router,
    user_router,
]

__all__ = [
    routers_list,
]
