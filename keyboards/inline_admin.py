from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.admin_lexicon import MENU_ADMIN, MENU_ADMIN_PANEL

# Создал объекты кнопок
menu_rules: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['rules_but'],
    callback_data='menu_rules_pressed'
)
menu_dues: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['dues_but'],
    callback_data='menu_dues_pressed'
)
menu_achievements: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['achievements'],
    callback_data='menu_achievements_pressed'
)
admin_panel_menu: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['admin_panel'],
    callback_data='admin_panel_menu_pressed'
)

statistics_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['statistics_but'],
    callback_data='statistics_but_pressed'
)
dues_manage_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['dues_manage_but'],
    callback_data='dues_manage_but_pressed'
)
users_manage_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['users_manag_but'],
    callback_data='users_manage_but_pressed'
)
come_back_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['come_back'],
    callback_data='come_back_but_pressed'
)

block_user_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN_PANEL['block_user'],
    callback_data='block_user_but_pressed'
)

mute_user_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN_PANEL['mute_user'],
    callback_data='mute_user_but_pressed'
)

give_level_max_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN_PANEL['give_level_max'],
    callback_data='give_level_max_but_pressed'
)

come_back_in_manage_user_but: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN['come_back'],
    callback_data='come_back_in_manage_user_but_pressed'
)
create_dues: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN_PANEL['create_dues'],
    callback_data='create_dues_pressed'
)
select_dues: InlineKeyboardButton = InlineKeyboardButton(
    text=MENU_ADMIN_PANEL['select_dues'],
    callback_data='select_dues_pressed'
)

admin_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[menu_rules, menu_dues],
                     [menu_achievements, admin_panel_menu]]
)
admin_panel_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[statistics_but, dues_manage_but],
                     [users_manage_but, come_back_but]]
)
user_manage_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[block_user_but, mute_user_but],
                     [give_level_max_but, come_back_in_manage_user_but]]
)
dues_manage_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[create_dues, select_dues]]
)
