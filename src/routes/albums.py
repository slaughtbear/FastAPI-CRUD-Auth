from fastapi import APIRouter, HTTPException
from src.models.albums import Album, AlbumUpdate, AlbumCreate, albums_list
from src.dependencies.albums import IdParam, QueryParam
from src.database.database import get_all_albums
from typing import List, Dict, Union


albums_router = APIRouter()


async def search_album(id: IdParam) -> Union[Album, None]:
    return next((album for album in albums_list if album.id == id), None)


@albums_router.get("/", response_model=List[Album])
async def get_albums() -> List[Album]:
    albums = await get_all_albums()
    return albums


@albums_router.get("/{id}", response_model=Album)
async def get_album(id: IdParam) -> Album:
    album = await search_album(id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    return album


@albums_router.get("/genre/", response_model=List[Album])
async def get_albums_by_genre(search: QueryParam) -> List[Album]:
    return [album for album in albums_list if album.genre.lower() == search.lower()]


@albums_router.get("/artist/", response_model=List[Album])
async def get_albums_by_artist(search: QueryParam) -> List[Album]:
    return [album for album in albums_list if album.artist.lower() == search.lower()]


@albums_router.post("/", response_model=Album, status_code=201)
async def create_album(album: AlbumCreate) -> Album:
    if await search_album(album.id):
        raise HTTPException(status_code=400, detail="El album ya existe")
    albums_list.append(album)
    return album


@albums_router.put("/{id}", response_model=Album)
async def update_album(id: IdParam, album: AlbumUpdate) -> Album:
    for index, item in enumerate(albums_list):
        if item.id == id:
            albums_list[index].title = album.title
            albums_list[index].artist = album.artist
            albums_list[index].year = album.year
            albums_list[index].genre = album.genre
            albums_list[index].rating = album.rating
            return albums_list[index]
    raise HTTPException(status_code=404, detail="Album no encontrado")


@albums_router.delete("/{id}")
async def delete_album(id: IdParam) -> Dict:
    album = await search_album(id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    albums_list.remove(album)
    return {"message": "Album eliminado"}