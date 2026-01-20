from fastapi import APIRouter, Form, UploadFile, File,HTTPException
import config.cloudinary_config 
from utils.cloudinary_upload import subir_imagen_cloudinary
from datetime import date
from services.producto_service import ProductoService
from models.producto_model import ProductoCreate,InventarioEntradaCreate,InventarioSalidaCreate,EntradaStock,ProductoUpdate

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

@router.put("/actualizar-precio")
def actualizar_precio(data: ProductoUpdate):
    service = ProductoService()
    return service.actualizar_precio_sync(data)

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
