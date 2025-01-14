from motor.motor_asyncio import AsyncIOMotorClient
from src.models.albums import Album
from decouple import config

mongodb_uri = config("MONGODB_URI")

client = AsyncIOMotorClient(mongodb_uri) # Conexión a la base de datos

database = client.apidb # Nombrando la base de datos

albums_collection = database.albums # Creando la colección para Albums

async def get_one_album_id(id: int):
    album = await albums_collection.find_one({"_id": id})
    return album

async def get_all_albums():
    albums = []
    cursor = albums_collection.find({})
    async for document in cursor:
        albums.append(Album(**document))
    return albums

async def create_album(album: Album):
    new_album = await albums_collection.insert_one(album)
    created_album = await albums_collection.find_one({"_id": new_album.inserted_id})
    return created_album

async def update_album(id: int, album: Album):
    await albums_collection.update_one({"_id": id}, {"$set": album})
    document = await albums_collection.find_one({"_id": id})
    return document

async def delete_album(id: int):
    await albums_collection.delete_one({"_id": id})
    return True