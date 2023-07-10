from sqlalchemy import Column, Integer, VARCHAR

from db.postgresql import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    name = Column(VARCHAR(50), unique=False, nullable=False)

    city = Column(VARCHAR(50), unique=False, nullable=False)

    def __str__(self) -> str:
        return f'User: {self.user_id}'