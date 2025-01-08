from pydantic import BaseModel
from typing import Optional

class Album(BaseModel): # Schema para consultar y registrar datos
    id: Optional[int]
    title: str
    artist: str
    year: int
    genre: str
    rating: float

class AlbumUpdate(BaseModel): # Schema para actualizar datos
    title: str
    artist: str
    year: int
    genre: str
    rating: float



albums_list = [
    Album(id=1, title="Nevermind", artist="Nirvana", year=1991, genre="Rock", rating=8.4),
    Album(id=2, title="All Eyez On Me", artist="2Pac", year=1996, genre="Rap", rating=8.0),
    Album(id=3, title="In Utero", artist="Nirvana", year=1992, genre="Rock", rating=8.0),
]