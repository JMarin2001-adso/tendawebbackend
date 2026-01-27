from fastapi import APIRouter
from services.cuadre_service import CuadreCajaService
from models.cuadre_model import CuadreCajaIn

router = APIRouter(
    prefix="/cuadre-caja",
    tags=["Cuadre de Caja"]
)

# 🔹 Ventas diarias (frontend)
@router.get("/ventas-diarias")
def ventas_diarias(fecha: str, id_usuario: int):
    service = CuadreCajaService()
    return service.obtener_ventas_diarias(fecha, id_usuario)


# 🔹 Guardar cuadre de caja
@router.post("/")
def guardar_cuadre(data: CuadreCajaIn):
    service = CuadreCajaService()
    return service.guardar_cuadre_caja(data)
