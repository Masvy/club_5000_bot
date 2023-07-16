from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Text

from filters.member_filters import IsStatus
from keyboards.reply_member import menu_member_kb
from keyboards.reply_without_status import menu_withaut_status_kb
from keyboards.inline_user import okay_kb
from db.users import read_status_member, read_name, read_donations
from lexicon.user_lexicon import USER_LEXICON

# Инициализировал роутер для данного модуля
router: Router = Router()

file_id = [
    'AgACAgIAAxkDAAIElGSv9ME7laADL8wTKuQFqrSZS'
    'hhHAALSyTEbTmBgSWiUvIVKpFmsAQADAgADeAADLwQ'
]

status_member_list: list[str] = ['Без статуса', 'Лайт', 'Стандарт', 'Макс']

router.message.filter(IsStatus(status_member_list))


# Этот хэндлер будет срабатывать на Callback
# с data 'okay_but_pressed'
@router.callback_query(Text(text='okay_but_pressed'))
async def show_menu_2(callback: CallbackQuery):
    status = await read_status_member(callback.from_user.id)
    name = await read_name(callback.from_user.id)
    if status == 'Без статуса':
        await callback.message.answer_photo(photo=file_id[0],
                                            caption=f'Привет, {name}👋\n\n'
                                            'Сайчас у тебя нет статуса.'
                                            ' Для получения минималнього'
                                            ' статуса ты должен задонатить'
                                            ' от 1000 рублей в месяц'
                                            f'{USER_LEXICON["greetings"]}',
                                            reply_markup=menu_withaut_status_kb)
    elif status == 'Лайт':
        await callback.message.answer_photo(photo=file_id[0],
                                            caption=f'Привет, {name}👋\n\n'
                                            'Сейчас твой уровень: Лайт\n\n'
                                            f'{USER_LEXICON["greetings"]}',
                                            reply_markup=menu_member_kb)
    elif status == 'Стандарт':
        await callback.message.answer_photo(photo=file_id[0],
                                            caption=f'Привет, {name}👋\n\n'
                                            'Сейчас твой уровень: Стандарт\n\n'
                                            f'{USER_LEXICON["greetings"]}',
                                            reply_markup=menu_member_kb)
    elif status == 'Макс':
        await callback.message.answer_photo(photo=file_id[0],
                                            caption=f'Привет, {name}👋\n\n'
                                            'Сейчас твой уровень: Макс\n\n'
                                            f'{USER_LEXICON["greetings"]}',
                                            reply_markup=menu_member_kb)


@router.message(Text(text='👑Статус'))
async def show_status(message: Message):
    status = await read_status_member(message.from_user.id)
    money = await read_donations(message.from_user.id)
    if status == 'Лайт':
        await message.answer('Твой уровень - ЛАЙТ\n\n'
                             f'Ты уже задонатил {money} рублей'
                             'на YY сборов\n\nТвои достижения:\n',
                             reply_markup=okay_kb)
    elif status == 'Стандарт':
        await message.answer('Твой уровень - СТАНДАРТ\n\n'
                             f'Ты уже задонатил {money} рублей'
                             'на YY сборов\n\nТвои достижения:\n',
                             reply_markup=okay_kb)
    elif status == 'Макс':
        await message.answer('Твой уровень - МАКС\n\n'
                             f'Ты уже задонатил {money} рублей'
                             'на YY сборов\n\nТвои достижения:\n',
                             reply_markup=okay_kb)
