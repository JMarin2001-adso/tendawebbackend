import config.cloudinary_config 
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from router.usuario_routes import routes as usuario_routes
from router.producto_routes import router as producto_routes
from router.envio_routes import router as envio_routes
from router.pedido_routes import router as pedido_routes
from router.auditoria_routes import router as auditoria_routes
from router.pago_routes import router as pago_routes
from router.factura_routes import router as factura_routes

app = FastAPI(title="tienda web")


app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
#app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Routers
app.include_router(usuario_routes)
app.include_router(producto_routes)
app.include_router(envio_routes)
app.include_router(pedido_routes)
app.include_router(auditoria_routes)
app.include_router(pago_routes)
app.include_router(factura_routes)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "https://tendawebfrontend-production.up.railway.app" 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK, tags=["APP"])
def message():
    return HTMLResponse("<h1>creacion de pagina</h1>")
