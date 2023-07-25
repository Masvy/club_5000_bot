from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создал объекты кнопок
phone_num_but: KeyboardButton = KeyboardButton(text='Отправить номер',
                                               request_contact=True)

phone_num_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[phone_num_but]],
    resize_keyboard=True)
