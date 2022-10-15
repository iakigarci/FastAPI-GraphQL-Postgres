from typing import Dict, Optional
from unicodedata import name
from db.postgres import get_db
from .models import Ad
from sqlalchemy.orm import Session
from fastapi import Depends

db : Session = get_db()


async def create_ad(name: str, amount: int, price: int) -> Dict:
    to_create = Ad(id=1002232323232, name=name, amount=amount, price=price)
    print("1111")
    db.add(to_create)
    print("2222")
    db.commit()
    print(to_create.id)
    print("333")
    return {
        "ID": to_create.id
    }

async def get_ad(id: int) -> Optional[Dict]:
    result = db.query(Ad).filter(Ad.id == id).first()  # type: ignore
    return {
        "success": True,
        "message": "Ad created successfully"
    }

