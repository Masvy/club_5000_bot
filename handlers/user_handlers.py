from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from lexicon.user_lexicon import USER_LEXICON

# Инициализировал роутер для данного модуля
router: Router = Router()


# Этот хэндлер отвечает на команду /start
@router.message(CommandStart())
async def start_user_bot(message: Message):
    await message.answer(text=USER_LEXICON['/start'])
