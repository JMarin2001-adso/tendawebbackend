from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    id_categoria: int
    categoria: str
    imagen: Optional[str] = None  # ruta (ej: "uploads/DOLCEGABANNA1.webp")

class EntradaStock(BaseModel):
    id_producto: int
    nombre_producto: Optional[str] = None
    precio_adquirido: float
    cantidad: int
    fecha_ingreso: date
    id_proveedor: Optional[int] = None
    observacion: Optional[str] = None

class InventarioSalidaCreate(BaseModel):
    id_producto: int
    cantidad: int
    fecha_salida: date
    observacion: Optional[str] = None
    id_usuario: int
    
class ProductoUpdate(BaseModel):
    id_producto: int
    nombre: str
    precio: float
    disponible: bool = True
    stock_actual:int
    imagen: Optional[str] = None

class ProductosUpdate(BaseModel):
    id_producto: int
    nombre: str
    precio: float
    imagen: Optional[str] = None