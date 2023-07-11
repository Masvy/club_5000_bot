from db import create_async_engine, get_session_maker
from config_data.config_db import ConfigDb, load_config_db
from sqlalchemy.engine import URL

config2: ConfigDb = load_config_db()

postgres_url = URL.create(
        'postgresql+asyncpg',
        username=config2.database.pg_user,
        password=config2.database.pg_password,
        database=config2.database.pg_db_name,
        host='localhost',
        port='5432'
    )


async_engine = create_async_engine(postgres_url)
session_maker = get_session_maker(async_engine)