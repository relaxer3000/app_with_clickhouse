from fastapi import APIRouter

from configurate import ocm
from models.py_user import UsersList, User
from rabbit.publisher import push_in_queue

user_router = APIRouter(tags=["user"])


@user_router.get("/", response_model=UsersList)
async def get_users() -> list[User]:
    result = ocm.get_user()
    return result


@user_router.post("/")
async def insert_user(user: User) -> dict:
    await push_in_queue(user)
    return {"message": "quest accepted"}
