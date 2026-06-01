from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Stock(BaseModel):
    productoId: int
    talla: str
    cantidad: int

stock_db = []

@router.get("/stock", response_model=List[Stock])
async def get_stock():
    return stock_db

@router.post("/stock", response_model=Stock)
async def create_stock(stock_item: Stock):
    stock_db.append(stock_item)
    return stock_item
