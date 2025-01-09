from fastapi import APIRouter, HTTPException, Path, Query
from src.models.albums import Album, AlbumUpdate, AlbumCreate, albums_list
from typing import List, Dict, Union


albums_router = APIRouter()


@albums_router.get("/", response_model=List[Album], tags=["Albums"])
async def get_albums() -> List[Album]:
    return albums_list


@albums_router.get("/{id}", response_model=Album, tags=["Albums"])
async def get_album(id: int = Path(gt=0)) -> Album:
    album = search_album(id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    return album


@albums_router.get("/genre/", response_model=List[Album], tags=["Albums"])
async def get_albums_by_genre(search: str = Query(min_length=3, max_length=64)) -> List[Album]:
    return [album for album in albums_list if album.genre.lower() == search.lower()]


@albums_router.get("/artist/", response_model=List[Album], tags=["Albums"])
async def get_albums_by_artist(search: str = Query(min_length=3, max_length=64)) -> List[Album]:
    return [album for album in albums_list if album.artist.lower() == search.lower()]


@albums_router.post("/", response_model=Album, status_code=201, tags=["Albums"])
async def create_album(album: AlbumCreate) -> Album:
    if search_album(album.id):
        raise HTTPException(status_code=400, detail="El album ya existe")
    albums_list.append(album)
    return album


@albums_router.put("/{id}", tags=["Albums"])
async def update_album(id: int, album: AlbumUpdate) -> Album:
    for index, item in enumerate(albums_list):
        if item.id == id:
            albums_list[index].title = album.title
            albums_list[index].artist = album.artist
            albums_list[index].year = album.year
            albums_list[index].genre = album.genre
            albums_list[index].rating = album.rating
            return albums_list[index]
    raise HTTPException(status_code=404, detail="Album no encontrado")


@albums_router.delete("/{id}", tags=["Albums"])
async def delete_album(id: int = Path(gt=0)) -> Dict:
    album = search_album(id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album no encontrado")
    albums_list.remove(album)
    return {"message": "Album eliminado"}
    

def search_album(id: int) -> Union[Album, None]:
    return next((album for album in albums_list if album.id == id), None)