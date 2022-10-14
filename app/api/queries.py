from typing import Optional

from ariadne import QueryType, convert_kwargs_to_snake_case

from app.db import crud

async def resolve_blogs(obj, info, skip: Optional[int] = 0, limit: Optional[int] = 100):
    storage = await crud.get_blogs(skip=skip, limit=limit)

    return {"blogs": storage}
