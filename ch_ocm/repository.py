from typing import Type

from sqlalchemy import engine, select, text
from sqlalchemy.orm import Session

from models.ocm_user import Base


class BaseCHRepo:
    def __init__(self, url: str):
        self.url = url
        self.engine = self._create_engine()

    def _create_engine(self):
        return engine.create_engine(self.url)


class CHRepo(BaseCHRepo):
    def __init__(self, url: str):
        super().__init__(url)
        self.session = self._create_session()

    def _create_session(self):
        return Session(self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)

    def _insert_data(self, py_data: dict, db_model: Type[Base]) -> None:
        data_db = db_model(**py_data)
        with self.session as session:
            session.add(data_db)
            session.commit()

    def _get_data(self, db_model: Type[Base]) -> list[dict]:
        with self.session as session:
            stmt = select(db_model)
            result_ocm = session.scalars(stmt).all()
            result_list = [result.to_dict() for result in result_ocm]
            return result_list


class CHDBIni(BaseCHRepo):

    def create_database(self, name: str):
        with self.engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {name}"))

    def drop_database(self, name: str):
        with self.engine.connect() as conn:
            conn.execute(text(f"DROP DATABASE IF EXISTS {name}"))
