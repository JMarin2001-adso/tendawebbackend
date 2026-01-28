from typing import List
from fastapi import APIRouter
from services.cuadre_service import CuadreCajaService
from models.cuadre_model import CuadreCajaIn

router = APIRouter(
    prefix="/cuadre-caja",
    tags=["Cuadre de Caja"]
)


@router.get("/ventas-diarias")
def ventas_diarias(fecha: str, id_usuario: int):
    service = CuadreCajaService()
    return service.obtener_ventas_diarias(fecha, id_usuario)

@router.post("/")
def guardar_cuadre(data: CuadreCajaIn):
    service = CuadreCajaService()
    return service.guardar_cuadre_caja(data)

@router.get("/cuadre-online")
def ventas_online_diarias(fecha: str):
    service = CuadreCajaService()
    return service.obtener_ventas_online(fecha)

@router.get("/existe")
def verificar_cuadre(fecha: str, id_usuario: int):
    service = CuadreCajaService()
    return service.verificar_existencia_cuadre(fecha, id_usuario)


