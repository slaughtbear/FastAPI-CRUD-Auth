from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    id: int
    username: str
    email: str

users_list: List[User] = [
    User(id=1, username="slaughtbear", email="slaughtbear@gmail.com"),
    User(id=2, username="ivan666", email="ivan.aguirre@gmail.com"),
]