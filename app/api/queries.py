from typing import Dict, Optional, Type
from ariadne import QueryType, convert_kwargs_to_snake_case
from db.models import Ad

from db import crud

def get_error(error):
    return {
        "success": False,
        "errors": [str(error)]
    }

async def resolve_storage(obj, info):
    try:
        storage = await crud.get_storage()
        return {"ads": storage}
    except Exception as error:
        return get_error(error)

async def resolve_ad(obj, info, id):
    try:
        ad = await crud.get_ad(id)
        if not ad:
            raise Exception("Ad not found")
        return {"ad": ad}
    except Exception as error:
        return get_error(error)

async def resolve_page(obj, info, term, perPage, nPage):
    try:
        ads = await crud.get_page(term, perPage, nPage)
        if len(ads) == 0:  # type: ignore
            return get_error("No ads found")
        next_page = nPage + 1 if (len(ads) / perPage) >= nPage else None  # type: ignore
        page = {
            "ads": ads,
            "total": len(ads),  # type: ignore
            "current": nPage,
            "nextPage": next_page
        }
        return {
            "page": page
        }
    except Exception as error:
        return get_error(error)

async def resolve_detail(obj, info, id):
    try:
        ad = await crud.get_ad(id)
        print(ad.name)
        if not ad:
            raise Exception("Ad not found")
        related_ads = await crud.get_related_ads(ad.uuid)  # type: ignore
        if not related_ads:
            raise Exception("No related ads found")
        return {
            "ad": ad,
            "relatedads": related_ads
        }
    except Exception as error:
        return get_error(error)

### QUERIES ###
query = QueryType()
query.set_field("getStorage", resolve_storage)
query.set_field("getAd", resolve_ad)
query.set_field("getPage", resolve_page)
query.set_field("getDetail", resolve_detail)
