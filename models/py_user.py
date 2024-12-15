from pydantic import BaseModel, Field


class User(BaseModel):
    username: str
    age: int = Field(gte=18, lt=128)

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "Ralf",
                "age": 25
            }
        }
    }


class UsersList(BaseModel):
    data: list[User] = Field(default_factory=list)
