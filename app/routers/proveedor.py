from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Proveedor(BaseModel):
    id: int
    nombre: str

proveedores_db = []

@router.get("/proveedores", response_model=List[Proveedor])
async def get_proveedores():
    return proveedores_db

@router.post("/proveedores", response_model=Proveedor)
async def create_proveedor(proveedor: Proveedor):
    proveedores_db.append(proveedor)
    return proveedor
