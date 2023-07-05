from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    '''
    Функция получает доступ к секретным данным

    Создал экземпляр класса Env
    Добавил в переменные окружения данные, прочитанные из файла .env
    Создал экземпляр класса Config
    '''
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))