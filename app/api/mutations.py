from ariadne import ObjectType, MutationType, convert_kwargs_to_snake_case
from db.models import Ad

from db import crud

mutation = ObjectType("Mutation")

@mutation.field("createAd")
async def resolve_create_ad(obj, info, uuid, name, amount: int = 0, price: int = 0, material: str = "Null"):
    try:
        ad_id = await crud.create_ad(Ad(uuid=uuid, name=name, amount=amount, price=price, material=material))
        return { "uuid": ad_id }
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

# The following 2 functions aren't finished yet, because the PK from the database wasn't well defined
@mutation.field("deleteAd")
async def resolve_delete_ad(obj, info, uuid):
    try:
        # await crud.delete_ad(uuid)
        return {
            "success": True
        }
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

@mutation.field("updateAd")
async def resolve_update_ad(obj, info, updateid, uuid, name, amount: int = 0, price: int = 0, material: str = "Null"):
    try:
        # await crud.update_ad(uuid, Ad(uuid=uuid, name=name, amount=amount, price=price, material=material))
        return {
            "success": True
        }
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

mutation = MutationType()
mutation.set_field("createAd", resolve_create_ad)
mutation.set_field("deleteAd", resolve_delete_ad)
mutation.set_field("updateAd", resolve_update_ad)