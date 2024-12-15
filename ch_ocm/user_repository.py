from ch_ocm.repository import CHRepo
from models.ocm_user import UserDB
from models.py_user import UsersList


class UserCHRepo(CHRepo):

    def insert_user(self, py_data: dict):
        self._insert_data(py_data, UserDB)

    def get_user(self) -> UsersList:
        list_of_users = self._get_data(UserDB)
        users_dict = {
            "data": list_of_users
        }
        return UsersList.model_validate(users_dict)
