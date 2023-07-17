from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text

from filters.member_filters import IsStatus
from db.users import read_status_member, read_name
from lexicon.user_lexicon import USER_LEXICON
from keyboards.reply_admin import admin_menu_kb

# Инициализировал роутер для данного модуля
router: Router = Router()

file_id = [
    'AgACAgIAAxkDAAIElGSv9ME7laADL8wTKuQFqrSZS'
    'hhHAALSyTEbTmBgSWiUvIVKpFmsAQADAgADeAADLwQ'
]

status_member_list: list[str] = ['Админ']

router.message.filter(IsStatus(status_member_list))


@router.callback_query(Text(text='okay_but_pressed'))
async def show_menu_3(callback: CallbackQuery):
    status = await read_status_member(callback.from_user.id)
    name = await read_name(callback.from_user.id)
    if status == 'Админ':
        await callback.message.answer_photo(photo=file_id[0],
                                            caption=f'Привет, {name}👋\n\n'
                                            'Сейчас твой уровень: Админ\n\n'
                                            f'{USER_LEXICON["greetings"]}',
                                            reply_markup=admin_menu_kb)
