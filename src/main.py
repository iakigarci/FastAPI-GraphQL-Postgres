from re import A
from unittest import result
from fastapi import FastAPI, HTTPException
from db.crud import Crud

crud_handler : Crud = Crud()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI for technical interview."} 

# Path: src\main.py
@app.get("/storage/")
async def get_storage(id: int):
    try:
        data = crud_handler.get_all_data()  # type: ignore
        return data
    except:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/ad/{id}")
async def get_ad(id: str):
    try:
        data = crud_handler.get_ad(id)  # type: ignore
        return data
    except:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/ads/")
async def get_page(term: str, per_page: int, page: int):
    try:
        ads = crud_handler.get_page(term, per_page, page)  # type: ignore
        # check if there is a next page.  
        next_page = page + 1 if (len(ads) / per_page) >= page else None
        result = {
            "ads": ads,
            "total": len(ads),
            "current": page,
            "nextPage": next_page,
        }
        return result
    except:
        raise HTTPException(status_code=404, detail="Item not found")