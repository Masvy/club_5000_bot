from aiogram.fsm.state import State, StatesGroup


class Verification(StatesGroup):
    number = State()
    name = State()
    city = State()
