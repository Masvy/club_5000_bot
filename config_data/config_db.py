from dataclasses import dataclass

from environs import Env


@dataclass
class Db:
    pg_user: str
    pg_password: str
    pg_db_name: str


@dataclass
class ConfigDb:
    database: Db


def load_config_db(path: str | None = None) -> ConfigDb:
    env = Env()
    env.read_env(path)
    return ConfigDb(database=Db(pg_user=env('PGUSER'), pg_password=env('PGPASSWORD'), pg_db_name=env('DB_NAME')))
