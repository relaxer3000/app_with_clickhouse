from clickhouse_sqlalchemy import engines
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class UserDB(Base):
    username: Mapped[str] = mapped_column(primary_key=True)
    age: Mapped[int] = mapped_column()

    __tablename__ = 'users'
    __table_args__ = (
        engines.Memory(),
    )

    def __repr__(self):
        return f"UserDB({self.username}, {self.age})"

    def to_dict(self):
        return_dict = {
            "username": self.username,
            "age": self.age,
        }
        return return_dict
