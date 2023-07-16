from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.user_lexicon import MENU_USER_LEXICON

# Создал объекты кнопок
menu_bit1: KeyboardButton = KeyboardButton(text=MENU_USER_LEXICON['rules_but'])
menu_but2: KeyboardButton = KeyboardButton(text=MENU_USER_LEXICON['join_but'])
menu_but3: KeyboardButton = KeyboardButton(text=MENU_USER_LEXICON['dues_but'])
menu_but4: KeyboardButton = KeyboardButton(text=MENU_USER_LEXICON['achievements'])

phone_num_but: KeyboardButton = KeyboardButton(text='Отправить номер', request_contact=True)

# Создал объект клавиатуры, добавил кнопки
menu_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[menu_bit1, menu_but2],
              [menu_but3, menu_but4]],
    resize_keyboard=True,
    one_time_keyboard=True)

phone_num_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[phone_num_but]],
    resize_keyboard=True)
