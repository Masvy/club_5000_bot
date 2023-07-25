from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from lexicon.user_lexicon import USER_LEXICON, DUES_LEXICON
from states.user_states import Verification, InputDues
from keyboards.reply_user import phone_num_kb
from db.users import add_user_id, add_name, add_city
from db.users import read_name, add_donations, read_registration_status
from db.users import read_donations, add_status_member
from db.users import add_registration_status, read_user_id
from keyboards.inline_user import dueses_kb, send_kb, okay_kb, menu_kb
from filters.member_filters import IsStatus

# Инициализировал роутер для данного модуля
router: Router = Router()

status_member_list: list[str] = ['Без статуса', 'Лайт',
                                 'Стандарт', 'Макс', 'Админ']


admins_ids: list[str] = ['707637895']


# Этот хэндлер отвечает на команду /start
# И переводить бота в состояние ожидания получения номера
@router.message(CommandStart(), StateFilter(default_state))
async def start_user_bot(message: Message, state: FSMContext):
    reg_status = await read_registration_status(message.from_user.id)
    if reg_status == 'Зарегистрирован':
        await message.answer('Ты уже зарегистрирован')
    else:
        await add_user_id(message.from_user.id)
        await message.answer(text=USER_LEXICON['/start'],
                             reply_markup=phone_num_kb)
        await state.set_state(Verification.number)


# Этот эндлер отлавливает номер
# И переводит бота в состояние ожидания ввода имени
@router.message(StateFilter(Verification.number))
async def process_number_sent(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer(text=USER_LEXICON['input_name'],
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Verification.name)


# Этот хэндлер отлавливает имя
# И переводит бота в состояние ожидания ввода города
@router.message(StateFilter(Verification.name))
async def process_name_sent(message: Message, state: FSMContext):
    _user_id = message.from_user.id
    name = message.text
    await add_name(_user_id, name)
    await state.update_data(name=message.text)
    await message.answer(text=USER_LEXICON['input_city'])
    await state.set_state(Verification.city)


# Это хендлер отлавливает город
# И выключает FSM
@router.message(StateFilter(Verification.city))
async def process_city_sent(message: Message, state: FSMContext):
    _user_id = message.from_user.id
    city_name = message.text
    user_id_db = await read_user_id(message.from_user.id)
    await state.update_data(city=message.text)
    await add_registration_status(_user_id, 'Зарегистрирован')
    await add_city(_user_id, city_name)
    if str(user_id_db) in admins_ids:
        await add_status_member(message.from_user.id, 'Админ')
    else:
        pass
    await message.answer(text=USER_LEXICON['FSM_finish'],
                         reply_markup=okay_kb)
    await state.clear()


# Этот хэндлер будет срабатывать на Callback
# с data 'okay_but_pressed'
@router.callback_query(F.data == 'okay_but_pressed',
                       ~IsStatus(status_member_list))
async def show_menu(callback: CallbackQuery):
    name_user = await read_name(callback.from_user.id)
    await callback.message.edit_text(text=f"Привет, {name_user}"
                                     f"\n\n{USER_LEXICON['greetings']}",
                                     reply_markup=menu_kb)


# Этот хэндлер отвечает на нажатие кнопки 'Правила'
@router.callback_query(F.data == 'menu_rules_pressed')
async def show_rules(callback: CallbackQuery):
    await callback.message.edit_text(text=USER_LEXICON['rules'],
                                     reply_markup=okay_kb)


# Этот хэндлер отвечает на нажатие кнопки 'Вступить'
@router.callback_query(F.data == 'menu_join_pressed')
async def join_func(callback: CallbackQuery):
    await callback.message.edit_text(text=USER_LEXICON['join'])
    await callback.message.answer(text=DUES_LEXICON['dueses_options'],
                                  reply_markup=dueses_kb)


# Этот хэндлер отвечает на нажатие кнопки 'Сборы'
@router.callback_query(F.data == 'menu_dues_pressed')
async def choice_of_dues(callback: CallbackQuery):
    await callback.message.edit_text(text=DUES_LEXICON['dueses_options'],
                                     reply_markup=dueses_kb)


# Этот хэндлер будет срабатывать на Callback
# с data 'dues_but_pressed'
@router.callback_query(F.data == 'dues_but_pressed')
async def dues_1_press(callback: CallbackQuery):
    await callback.message.edit_text(text='Название\n\nОписание',
                                     reply_markup=send_kb)


# Этот хэндлер будет срабатывать на Callback
# с data 'send_dues_but_pressed'
@router.callback_query(F.data == 'send_dues_but_pressed',
                       StateFilter(default_state))
async def send_dues_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=DUES_LEXICON['input_dues'])
    await state.set_state(InputDues._sum)


# Этот хэндлер срабатывает на введение суммы доната
@router.message(StateFilter(InputDues._sum),
                lambda x: x.text.isdigit() and int(x.text) > -1 and
                int(x.text) < 20000)
async def input_sum(message: Message, state: FSMContext):
    donation = message.text
    await add_donations(message.from_user.id, int(donation))
    all_donation = await read_donations(message.from_user.id)
    if 1 <= all_donation < 1000:
        await add_status_member(message.from_user.id, 'Без статуса')
    elif 1000 <= all_donation < 5000:
        await add_status_member(message.from_user.id, 'Лайт')
    elif 5000 <= all_donation < 100000:
        await add_status_member(message.from_user.id, 'Стандарт')
    else:
        await add_status_member(message.from_user.id, 'Макс')
    await state.update_data(_sum=message.text)
    await message.answer(text=DUES_LEXICON['gratitude'],
                         reply_markup=okay_kb)
    await state.clear()


# Этот хэндлер срабатывает на ввведение доната, который
# Больше 20к
@router.message(StateFilter(InputDues._sum),
                lambda x: x.text.isdigit() and int(x.text) >= 20000)
async def input_sum_more_20k(message: Message):
    await message.answer(text='Мы не приминимет суммы больше 20к')


# Этот хэндлер срабатывает на введение некоректной суммы
# Например, вместо цифры вводятся буквы
@router.message(StateFilter(InputDues._sum))
async def wrong_input_sum(message: Message):
    await message.answer(text=DUES_LEXICON['incorrect_num'])


# Этот хэндлер будет срабатывать на Callback
# с data 'send_cancel_dues_but_pressed'
@router.callback_query(F.data == 'send_cancel_dues_but_pressed')
async def send_cancel_dues_press(callback: CallbackQuery):
    await callback.message.answer(text=DUES_LEXICON['dueses_options'],
                                  reply_markup=dueses_kb)


@router.callback_query(F.data == 'menu_achievements_pressed')
async def show_achievement(callback: CallbackQuery):
    await callback.message.edit_text(text=USER_LEXICON['show_achievements'],
                                     reply_markup=okay_kb)
