from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.member_lexicon import MENU_MEMBER

# Создал объекты кнопок
menu_bit1: KeyboardButton = KeyboardButton(text=MENU_MEMBER['rules_but'])
menu_but2: KeyboardButton = KeyboardButton(text=MENU_MEMBER['status_but'])
menu_but3: KeyboardButton = KeyboardButton(text=MENU_MEMBER['dues_but'])
menu_but4: KeyboardButton = KeyboardButton(text=MENU_MEMBER['achievements'])

# Создал объект клавиатуры, добавил кнопки
menu_member_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[menu_bit1, menu_but2],
              [menu_but3, menu_but4]],
    resize_keyboard=True,
    one_time_keyboard=True)