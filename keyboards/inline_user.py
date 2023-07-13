from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.user_lexicon import DUES_LEXICON, USER_LEXICON


okay_but: InlineKeyboardButton = InlineKeyboardButton(
    text=USER_LEXICON['okay'],
    callback_data='okay_but_pressed'
)


dues_but: InlineKeyboardButton = InlineKeyboardButton(
    text=DUES_LEXICON['dues_but'],
    callback_data='dues_but_pressed'
)

send_dues_but: InlineKeyboardButton = InlineKeyboardButton(
    text=DUES_LEXICON['send_dues'],
    callback_data='send_dues_but_pressed'
)

send_cancel_dues_but: InlineKeyboardButton = InlineKeyboardButton(
    text=DUES_LEXICON['cancel_send'],
    callback_data='send_cancel_dues_but_pressed'
)

okay_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[okay_but]]
)

dueses_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[dues_but]]
)

send_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[send_dues_but, send_cancel_dues_but]]
)