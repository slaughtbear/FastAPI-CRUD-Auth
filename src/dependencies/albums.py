from fastapi import Query, Path, Depends
from typing import Annotated


async def get_id_param(id: int = Path(gt=0)) -> int:
    return id


IdParam = Annotated[int, Depends(get_id_param)]
QueryParam = Annotated[str, Query(min_length=3, max_length=64)]
