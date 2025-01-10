from fastapi import FastAPI
from src.routes.albums import albums_router
from src.routes.users import users_router

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello World"}

app.include_router(albums_router, prefix="/albums", tags=["Albums"])
app.include_router(users_router, prefix="/users", tags=["Users"])