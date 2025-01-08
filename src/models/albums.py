from pydantic import BaseModel, Field
from typing import List
import datetime

current_date = datetime.date.today().year

class Album(BaseModel): # Schema para consultar
    id: int
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


class AlbumCreate(BaseModel): # Schema para registrar datos
    id: int = Field(ge=0)
    title: str = Field(min_length=3, max_length=64, default="Album")
    artist: str = Field(min_length=3, max_length=32, default="Artist")
    year: int = Field(ge=1970, le=current_date, default=current_date)
    genre: str = Field(min_length=3, max_length=32, default="Genre")
    rating: float = Field(ge=0.0, le=10.0, default=0.0)


albums_list: List[Album] = [
    Album(id=1, title="Nevermind", artist="Nirvana", year=1991, genre="Rock", rating=8.4),
    Album(id=2, title="All Eyez On Me", artist="2Pac", year=1996, genre="Rap", rating=8.0),
    Album(id=3, title="In Utero", artist="Nirvana", year=1992, genre="Rock", rating=8.0),
]