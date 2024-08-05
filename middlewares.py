from typing import Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

import config
from db.base import add_user
from loader import db_connector


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ):
        user = data['event_from_user']
        await add_user(
            db_connector=db_connector,
            tg_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            is_admin=(user.id == int(config.ADMIN_ID))
        )
        return await handler(event, data)
