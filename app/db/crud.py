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
    return to_create.uuid  # type: ignore

async def get_ad(uuid: str) -> Ad:
    return db.query(Ad).filter(Ad.uuid == uuid).first()  # type: ignore

async def get_storage() -> Optional[Dict]:
    return db.query(Ad).all()  # type: ignore

async def get_page(term: str, perPage: int, nPage: int) -> Optional[Dict]:
    return db.query(Ad).filter(Ad.name.contains(term)).limit(perPage).offset(nPage * perPage).all()  # type: ignore

async def get_related_ads(id: str):
    material = db.query(Ad).filter(Ad.uuid == id).first()  # type: ignore
    return db.query(Ad).filter(Ad.uuid != id, Ad.material == material.material).all()  # type: ignore
