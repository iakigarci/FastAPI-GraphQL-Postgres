import re
from typing import Dict, Optional
from unicodedata import name
from db.postgres import get_db
from .models import Ad
from sqlalchemy.orm import Session
from fastapi import Depends

db = get_db()

async def create_ad(name: str, amount: int, price: int) -> int:
    to_create = Ad(name=name, amount=amount, price=price)
    db.add(to_create)
    db.commit()
    return to_create.id  # type: ignore

async def get_ad(id: int) -> Ad:
    return db.query(Ad).filter(Ad.id == id).first()  # type: ignore

async def get_storage() -> Optional[Dict]:
    return db.query(Ad).all()  # type: ignore

async def get_page(term: str, perPage: int, nPage: int) -> Optional[Dict]:
    return db.query(Ad).filter(Ad.name.contains(term)).limit(perPage).offset(nPage * perPage).all()  # type: ignore
