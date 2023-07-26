from sqlalchemy import Column, Integer, VARCHAR, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, update, select

from db.postgresql import BaseModel
from loader import session_maker


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)

    name = Column(VARCHAR(50), unique=False, nullable=True)

    city = Column(VARCHAR(50), unique=False, nullable=True)

    donations = Column(Integer, unique=False, default=0)

    status_member = Column(VARCHAR(30), unique=False, default='Вне клуба')

    registration_status = Column(VARCHAR(20), unique=False,
                                 default='Не зарегистрирован')

    block_status = Column(VARCHAR(25), unique=False,
                          default='Не заблокирован')

    def __str__(self) -> str:
        return f'User: {self.user_id}'


async def add_user_id(_user_id):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(insert(User).values(user_id=_user_id))


async def add_name(_user_id, name):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == _user_id).values(name=name))


async def add_city(_user_id, city):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == _user_id).values(city=city))


async def add_donations(_user_id, donation):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == _user_id).values(donations=User.donations+donation))


async def add_status_member(_user_id, _status_member):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == _user_id).values(status_member=_status_member))


async def add_registration_status(_user_id, _registration_status):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == _user_id).values(registration_status=_registration_status))


async def add_block_status(_user_id, _block_status):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == _user_id).values(block_status=_block_status))


async def read_name(_user_id):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.name).where(User.user_id == _user_id))
            name = result.scalar()
    return name


async def read_donations(_user_id):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.donations).where(User.user_id == _user_id))
            donations = result.scalar()
    return donations


async def read_status_member(_user_id):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.status_member).where(User.user_id == _user_id))
            status_memeber = result.scalar()
    return status_memeber


async def read_registration_status(_user_id):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.registration_status).where(User.user_id == _user_id))
            registration_status = result.scalar()
    return registration_status


async def read_user_id(_user_id):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_id).where(User.user_id == _user_id))
            _user_id_db = result.scalar()
    return _user_id_db
