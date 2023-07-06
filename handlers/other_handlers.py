from aiogram import Router
from aiogram.types import Message

from lexicon.user_lexicon import USER_LEXICON

# Инициализировал роутер для данного модуля
router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=USER_LEXICON['other_answer'])
