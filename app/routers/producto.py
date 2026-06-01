from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

productos_db = []

@router.get("/productos", response_model=List[Producto])
async def get_productos():
    return productos_db

@router.post("/productos", response_model=Producto)
async def create_producto(producto: Producto):
    productos_db.append(producto)
    return producto

@router.delete("/productos/{producto_id}", response_model=Producto)
async def delete_producto(producto_id: int):
    producto = next((p for p in productos_db if p.id == producto_id), None)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    productos_db.remove(producto)
    return producto
