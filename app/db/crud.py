from typing import Dict, Optional
from unicodedata import name
from db.postgres import get_db
from .models import Ad
from sqlalchemy.orm import Session
from fastapi import Depends

# db : Session = Depends(get_db)
db = get_db()

async def create_ad(id: int, name: str, amount: int, price: int) -> Dict:
    try:
        to_create = Ad(id=id, name=name, amount=amount, price=price)
        print("1111")
        db.add(to_create)
        print("2222")
        db.commit()
        print(to_create.id)
        print("333")
        return {
            "ID": to_create.id
        }
    except Exception as error:
        print(error)
        return {
            "error": str(error)
        }

async def get_ad(id: int) -> Optional[Dict]:
    result = db.query(Ad).filter(Ad.id == id).first()  # type: ignore
    return {
        "success": True,
        "message": "Ad created successfully"
    }

