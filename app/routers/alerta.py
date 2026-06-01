from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Alerta(BaseModel):
    id: int
    productoId: int
    cantidad: int

alertas_db = []

@router.get("/alertas", response_model=List[Alerta])
async def get_alertas():
    return alertas_db

@router.post("/alertas", response_model=Alerta)
async def create_alerta(alerta: Alerta):
    alertas_db.append(alerta)
    return alerta
