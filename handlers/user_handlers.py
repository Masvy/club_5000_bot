from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from lexicon.user_lexicon import USER_LEXICON
from states.user_states import Verification

# Инициализировал роутер для данного модуля
router: Router = Router()


# Этот хэндлер отвечает на команду /start
# И переводить бота в состояние ожидания ввода номера
@router.message(CommandStart(), StateFilter(default_state))
async def start_user_bot(message: Message, state: FSMContext):
    await message.answer(text=USER_LEXICON['/start'])
    await state.set_state(Verification.number)


# Этот эндлер отлавливает номер
# И переводит бота в состояние ожидания ввода имени
@router.message(StateFilter(Verification.number))
async def process_number_sent(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer(text=USER_LEXICON['input_name'])
    await state.set_state(Verification.name)


# Этот хэндлер отлавливает имя
# И переводит бота в состояние ожидания ввода города
@router.message(StateFilter(Verification.name))
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=USER_LEXICON['input_city'])
    await state.set_state(Verification.city)


# Это хендлер отлавливает город
# И выключает FSM
@router.message(StateFilter(Verification.city))
async def process_city_sent(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text=USER_LEXICON['FSM_finish'])
    await state.clear()
