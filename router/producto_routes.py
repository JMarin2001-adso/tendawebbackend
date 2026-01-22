from fastapi import APIRouter, Form, UploadFile, File,HTTPException
from fastapi.responses import JSONResponse
from utils.cloudinary_upload import subir_imagen_cloudinary
from datetime import date
from services.producto_service import ProductoService
from models.producto_model import ProductoCreate,ProductosUpdate,InventarioEntradaCreate,InventarioSalidaCreate,EntradaStock,ProductoUpdate

router = APIRouter(prefix="/producto", tags=["Producto"])


@router.post("/")
async def crear_producto(
    nombre: str = Form(...),
    descripcion: str = Form(...),
    precio: float = Form(...),
    id_categoria: int = Form(...),
    categoria: str = Form(...),
    imagen: UploadFile = File(None)
):
    imagen_url = None

    if imagen:
        imagen_url = subir_imagen_cloudinary(imagen.file)

    producto = ProductoCreate(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        id_categoria=id_categoria,
        categoria=categoria,
        imagen=imagen_url
    )

    service = ProductoService()
    return service.crear_producto(producto)

@router.get("/")
def listar_productos():
    service = ProductoService()  
    return service.listar_productos_sync()

@router.post("/entrada")
def registrar_entrada(data: InventarioEntradaCreate):
    service = ProductoService()
    return service.agregar_entrada_sync(data)


@router.post("/salida")
def registrar_salida(data: InventarioSalidaCreate):
    service = ProductoService()
    return service.agregar_salida_sync(data)

@router.get("/entradas")
def listar_entradas():
    service = ProductoService()
    return service.listar_entradas_sync()


@router.get("/salidas")
def listar_salidas():
    service = ProductoService()
    return service.listar_salidas_sync()

@router.get("/inventario")
def listar_inventario():
    service = ProductoService()
    return service.listar_inventario_sync()

@router.post("/entrada-stock")
def entrada_stock(data: EntradaStock):
    service = ProductoService()
    return service.entrada_stock_sync(data)

@router.post("/sincronizar-inventario")
def sincronizar_inventario():
    service = ProductoService()
    return service.sincronizar_inventario_sync()


from fastapi import HTTPException, status

@router.put("/actualizar-producto")
async def actualizar_producto(
    id_producto: int = Form(...),
    nombre: str = Form(...),
    precio: float = Form(...),
    imagen: UploadFile = File(None)
):
    imagen_url = None

    if imagen and imagen.filename:
        try:
            imagen_url = subir_imagen_cloudinary(imagen.file)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=f"Error al subir imagen: {str(e)}"
            )

    producto = ProductosUpdate(
        id_producto=id_producto,
        nombre=nombre,
        precio=precio,
        imagen=imagen_url
    )

    service = ProductoService()
    resultado = service.actualizar_producto(producto)

    if not resultado["success"]:
        if "no encontrado" in resultado["message"].lower():
            raise HTTPException(status_code=404, detail=resultado["message"])
        raise HTTPException(status_code=400, detail=resultado["message"])

    return resultado

@router.get("/productos-mayor-rotacion")
def productos_mayor_rotacion(
    fecha_inicio: date | None = None,
    fecha_fin: date | None = None
):
    service = ProductoService()
    return service.productos_mayor_rotacion_sync(fecha_inicio, fecha_fin)

@router.get("/productos-bajo-stock")
def productos_bajo_stock():
    service = ProductoService()
    return service.productos_bajo_stock_sync()
