from fastapi import APIRouter, HTTPException, Path, Query
from src.models.users import User, users_list
from typing import List

users_router = APIRouter()

@users_router.get("/", response_model=List[User], tags=["Users"])
async def get_users() -> List[User]:
    return users_list