from pydantic import BaseModel
from datetime import date,datetime
from typing import List, Optional

class CuadreCajaIn(BaseModel):
    fecha: date
    id_empleado: int
    total_sistema: float
    dinero_caja: float
    observacion: Optional[str] = None


class VentaDiariaOut(BaseModel):
    id_factura: int
    numero_factura: str
    total: float
    fecha: str


class VentaOnlineOut(BaseModel):
    id_factura: int
    numero_factura: str
    total: float
    fecha: datetime
    id_empleado: int


class ReporteOnlineResponse(BaseModel):
    success: bool
    ventas: List[VentaOnlineOut]
    total_online: float
