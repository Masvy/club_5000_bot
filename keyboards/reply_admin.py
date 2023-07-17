from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.admin_lexicon import MENU_ADMIN

# Создал объекты кнопок
menu_but1: KeyboardButton = KeyboardButton(text=MENU_ADMIN['rules_but'])
menu_but2: KeyboardButton = KeyboardButton(text=MENU_ADMIN['dues_but'])
menu_but3: KeyboardButton = KeyboardButton(text=MENU_ADMIN['achievements'])
menu_but4: KeyboardButton = KeyboardButton(text=MENU_ADMIN['statistics_but'])
menu_but5: KeyboardButton = KeyboardButton(text=MENU_ADMIN['dues_manag_but'])
menu_but6: KeyboardButton = KeyboardButton(text=MENU_ADMIN['users_manag_but'])
menu_but7: KeyboardButton = KeyboardButton(text=MENU_ADMIN['come_back'])

admin_menu_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[menu_but1, menu_but2, menu_but3],
              [menu_but4, menu_but5, menu_but6],
              [menu_but7]]
)
