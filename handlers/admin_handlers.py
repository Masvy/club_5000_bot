from aiogram import Router, F
from aiogram.types import CallbackQuery

from filters.member_filters import IsStatus
from db.users import read_name
from lexicon.user_lexicon import USER_LEXICON
from lexicon.admin_lexicon import MENU_ADMIN_PANEL
from keyboards.inline_admin import admin_menu_kb, admin_panel_menu_kb, user_manage_kb

# Инициализировал роутер для данного модуля
router: Router = Router()


status_member_list: list[str] = ['Админ']


@router.callback_query(F.data == 'okay_but_pressed',
                       IsStatus(status_member_list))
async def show_menu_3(callback: CallbackQuery):
    name = await read_name(callback.from_user.id)
    await callback.message.edit_text(text=f'Привет, {name}👋\n\n'
                                     'Сейчас твой уровень: Админ\n\n'
                                     f'{USER_LEXICON["greetings"]}',
                                     reply_markup=admin_menu_kb)


@router.callback_query(F.data == 'admin_panel_menu_pressed')
async def show_admin_panel(callback: CallbackQuery):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['show_admin_panel'],
                                     reply_markup=admin_panel_menu_kb)


@router.callback_query(F.data == 'statistics_but_pressed')
async def show_stat(callback: CallbackQuery):
    await callback.message.edit_text(text='Статистика проекта:\n\n'
                                     'Сборов: \n\n'
                                     'Пользователей (прошедших регистрацию):'
                                     '\n\nВне клуба:\nЛайт:\nСтандарт:\n'
                                     'Макс:\nАмбассадоров:\n\nАктивных:\n'
                                     'за неделю:\nза месяц:\n\nСобрано'
                                     ' средств:\nза неделю\nза месяц:',
                                     reply_markup=admin_panel_menu_kb)


@router.callback_query(F.data == 'users_manage_but_pressed')
async def show_users_manage(callback: CallbackQuery):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['users_manage_panel'],
                                     reply_markup=user_manage_kb)


@router.callback_query(F.data == 'block_user_but_pressed')
async def func_block_user(callback: CallbackQuery):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['input_user_id'])


@router.callback_query(F.data == 'come_back_but_pressed')
async def back_to_main_menu(callback: CallbackQuery):
    name = await read_name(callback.from_user.id)
    await callback.message.edit_text(text=f'Привет, {name}👋\n\n'
                                     'Сейчас твой уровень: Админ\n\n'
                                     f'{USER_LEXICON["greetings"]}',
                                     reply_markup=admin_menu_kb)