import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from db import BaseModel, proceed_schemas
from loader import session_maker, async_engine

# Инициализировал логгер
logger = logging.getLogger(__name__)


async def main():
    '''
    Функция конфигурирования и запуска бота

    Конфигурировал логирование
    Вывел в консоль информацию о начале запуска бота
    Загрузил конфиг в переменную config
    Инициализировал Redis
    Инициализировал хранилище
    Создал объекты бота и диспетчера
    Регистриуем роутеры в диспетчере
    Пропускаем накопившиеся апдейты и запускаем polling
    '''
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    redis: Redis = Redis(host='localhost')

    storage: RedisStorage = RedisStorage(redis=redis)

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)

    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot, session_maker=session_maker)

if __name__ == '__main__':
    asyncio.run(main())