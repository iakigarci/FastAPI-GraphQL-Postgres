from typing import Optional

from ariadne import QueryType, convert_kwargs_to_snake_case

from db import crud

async def resolve_ad(obj, info, **kwargs):
    # result = crud.get_ad(kwargs["id"])
    return {"adaaas": 11}

async def resolve_storage(obj, info):
    storage = crud.get_storage()
    return {"ads": storage}

query = QueryType()
query.set_field("storage", resolve_storage)
query.set_field("ad", resolve_ad)
