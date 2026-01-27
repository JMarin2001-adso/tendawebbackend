from pydantic import BaseModel
from datetime import date
from typing import Optional

class CuadreCajaIn(BaseModel):
    fecha: date
    id_usuario: int
    total_sistema: float
    dinero_caja: float
    observacion: Optional[str] = None


class VentaDiariaOut(BaseModel):
    id_factura: int
    numero_factura: str
    total: float
    fecha: str
