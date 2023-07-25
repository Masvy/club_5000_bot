from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.member_lexicon import MENU_MEMBER

# Создал объекты кнопок
menu_rules: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_MEMBER['rules_but'],
    callback_data='menu_rules_pressed')
menu_status: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_MEMBER['status_but'],
    callback_data='menu_status_pressed')
menu_dues: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_MEMBER['dues_but'],
    callback_data='menu_dues_pressed'
)
menu_achievements: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_MEMBER['achievements'],
    callback_data='menu_achievements_pressed'
)

# Создал объект клавиатуры, добавил кнопки
menu_member_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[menu_rules, menu_status],
                     [menu_dues, menu_achievements]]
)
