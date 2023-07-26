from aiogram.fsm.state import State, StatesGroup


# Создал класс для группы состояний
class InputIdForBlock(StatesGroup):
    user_id_block = State()


# Создал класс для группы состояний
class InputIdForGivaMax(StatesGroup):
    user_id_give_max = State()


# Создал класс для группы состояний
class InputNameForDues(StatesGroup):
    dues_name = State()
