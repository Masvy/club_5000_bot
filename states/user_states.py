from aiogram.fsm.state import State, StatesGroup


# Создал класс для группы состояний
class Verification(StatesGroup):
    number = State()
    name = State()
    city = State()


# Создал класс для группы состояний
class InputDues(StatesGroup):
    _sum = State()