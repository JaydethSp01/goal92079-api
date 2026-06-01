from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Categoria(BaseModel):
    id: int
    nombre: str

categorias_db = []

@router.get("/categorias", response_model=List[Categoria])
async def get_categorias():
    return categorias_db

@router.post("/categorias", response_model=Categoria)
async def create_categoria(categoria: Categoria):
    categorias_db.append(categoria)
    return categoria
