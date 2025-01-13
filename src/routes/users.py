from fastapi import APIRouter, HTTPException, Path, Query
from src.models.users import User, users_list
from typing import Union, List


users_router = APIRouter()


@users_router.get("/", response_model=List[User])
async def get_users() -> List[User]:
    return users_list


@users_router.get("/{id}", response_model=User)
async def get_user(id: int = Path(gt=0)) -> User:
    user = search_user(id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


def search_user(id: int) -> Union[User, None]:
    return next((user for user in users_list if user.id == id), None)