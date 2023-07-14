from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text

from filters.member_filters import IsStatus
from keyboards.reply_member import menu_member_kb
from db.users import read_status_member, read_name

# Инициализировал роутер для данного модуля
router: Router = Router()

file_id = [
    'AgACAgIAAxkDAAIElGSv9ME7laADL8wTKuQFqrSZS'
    'hhHAALSyTEbTmBgSWiUvIVKpFmsAQADAgADeAADLwQ'
]

status_member_list: list[str] = ['Лайт', 'Стандарт', 'Макс']

router.message.filter(IsStatus(status_member_list))


# Этот хэндлер будет срабатывать на Callback
# с data 'okay_but_pressed'
@router.callback_query(Text(text='okay_but_pressed'))
async def show_menu_2(callback: CallbackQuery):
    status = await read_status_member(callback.from_user.id)
    name = await read_name(callback.from_user.id)
    if status == 'Лайт':
        await callback.message.answer(f'Привет, {name}\n\n'
                                      'Сейчас твой уровень: Лайт',
                                      reply_markup=menu_member_kb)
    elif status == 'Стандарт':
        await callback.message.answer(f'Привет, {name}\n\n'
                                      'Сейчас твой уровень: Стандарт',
                                      reply_markup=menu_member_kb)
    elif status == 'Макс':
        await callback.message.answer(f'Привет, {name}\n\n'
                                      'Сейчас твой уровень: Макс',
                                      reply_markup=menu_member_kb)
