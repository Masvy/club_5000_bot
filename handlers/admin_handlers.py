from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from filters.member_filters import IsStatus
from db.users import read_name, add_block_status, add_status_member
from lexicon.user_lexicon import USER_LEXICON
from lexicon.admin_lexicon import MENU_ADMIN_PANEL
from keyboards.inline_admin import admin_menu_kb, admin_panel_menu_kb
from keyboards.inline_admin import user_manage_kb, dues_manage_kb
from states.admin_states import InputIdForBlock, InputIdForGivaMax
from states.admin_states import InputNameForDues

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


@router.callback_query(F.data == 'dues_manage_but_pressed')
async def show_dues_manage(callback: CallbackQuery):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['dues_manage_panel'],
                                     reply_markup=dues_manage_kb)


@router.callback_query(F.data == 'create_dues_pressed',
                       StateFilter(default_state))
async def request_name_dues(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['request_dues_name'])
    await state.set_state(InputNameForDues.dues_name)


@router.message(StateFilter(InputNameForDues.dues_name))
async def input_name_dues(message: Message, state: FSMContext):
    await state.update_data(dues_name=message.text)
    await message.answer(text=MENU_ADMIN_PANEL['dues_created'],
                         reply_markup=dues_manage_kb)
    await state.clear()


@router.callback_query(F.data == 'users_manage_but_pressed')
async def show_users_manage(callback: CallbackQuery):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['users_manage_panel'],
                                     reply_markup=user_manage_kb)


@router.callback_query(F.data == 'give_level_max',
                       StateFilter(default_state))
async def request_user_id_for_give_max(callabck: CallbackQuery, state: FSMContext):
    await callabck.message.edit_text(text=MENU_ADMIN_PANEL['request_user_id'])
    await state.set_state(InputIdForGivaMax.user_id_give_max)


@router.message(StateFilter(InputIdForGivaMax.user_id_give_max))
async def input_user_id_for_give_max(message: Message, state: FSMContext):
    await add_status_member(int(message.text), 'Макс')
    await state.update_data(user_id_give_max=message.text)
    await message.answer(MENU_ADMIN_PANEL['appointed'],
                         reply_markup=user_manage_kb)
    await state.clear()


@router.callback_query(F.data == 'block_user_but_pressed',
                       StateFilter(default_state))
async def request_user_id_for_block(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=MENU_ADMIN_PANEL['request_user_id'])
    await state.set_state(InputIdForBlock.user_id_block)


@router.message(StateFilter(InputIdForBlock.user_id_block))
async def input_user_id_for_block(message: Message, state: FSMContext):
    await add_block_status(int(message.text), 'Заблокирован')
    await state.update_data(user_id_block=message.text)
    await message.answer(MENU_ADMIN_PANEL['blocked'],
                         reply_markup=user_manage_kb)
    await state.clear()


@router.callback_query(F.data == 'come_back_but_pressed')
async def back_to_main_menu(callback: CallbackQuery):
    name = await read_name(callback.from_user.id)
    await callback.message.edit_text(text=f'Привет, {name}👋\n\n'
                                     'Сейчас твой уровень: Админ\n\n'
                                     f'{USER_LEXICON["greetings"]}',
                                     reply_markup=admin_menu_kb)
