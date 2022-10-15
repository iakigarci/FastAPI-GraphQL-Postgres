from ariadne import ObjectType, MutationType, convert_kwargs_to_snake_case

from db import crud

mutation = ObjectType("Mutation")

@mutation.field("createUser")
async def resolve_create_ad(obj, info,name, amount, price):
    try:
        ad_id = await crud.create_ad(name=name, amount=amount, price=price)
        return { "id": ad_id }
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

mutation = MutationType()
mutation.set_field("createAd", resolve_create_ad)