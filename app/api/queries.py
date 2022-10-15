from typing import Optional, Type
from ariadne import QueryType, convert_kwargs_to_snake_case

from db import crud


async def resolve_storage(obj, info):
    try:
        storage = await crud.get_storage()
        return {"ads": storage}
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }


async def resolve_ad(obj, info, id):
    try:
        ad = await crud.get_ad(id)
        if not ad:
            raise Exception("Ad not found")
        return {"ad": ad}
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

async def resolve_page(obj, info, term, perPage, nPage):
    try:
        ads = await crud.get_page(term, perPage, nPage)
        if not ads:
            raise Exception("Page not found")
        page = {
            "ads": ads,
            "total": len(ads),
            "current": nPage,
            "nextPage": nPage + 1
        }
        return {
            "page": page
        }
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

query = QueryType()
query.set_field("getStorage", resolve_storage)
query.set_field("getAd", resolve_ad)
query.set_field("getPage", resolve_page)
