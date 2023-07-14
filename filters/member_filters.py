from aiogram.filters import BaseFilter
from aiogram.types import Message

from db.users import read_status_member


class IsStatus(BaseFilter):
    def __init__(self, status_member_list: list[str]) -> None:
        self.status_member_list = status_member_list

    async def __call__(self, message: Message) -> bool:
        status = await read_status_member(message.from_user.id)
        return status in self.status_member_list