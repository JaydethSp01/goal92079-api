from pydantic import BaseModel, Field
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    nombre: str
    precio: float

class Categoria(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    nombre: str

class Stock(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    producto_id: int
    talla: str
    cantidad: int

class Proveedor(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    nombre: str
    contacto: str

class Alerta(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    producto_id: int
    mensaje: str
