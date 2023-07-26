from typing import Any, Awaitable, Callable, Dict, Union
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from loader import session_maker
from db.users import User


class BlockCheck(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        _session_maker: sessionmaker = session_maker
        async with _session_maker() as session:
            async with session.begin():
                result = await session.execute(select(User.block_status).where(User.user_id == event.from_user.id))
                user: User = result.scalar()

                if user == 'Заблокирован':
                    await event.answer('Ты был заблокирован')
                    return
                else:
                    pass

        return await handler(event, data)