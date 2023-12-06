from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import httpx
import os

# Es preciso indicarle una url de backend, sino utilizara 127.0.0.1:10000
BASE_URL = os.getenv('BASE_URL', 'http://127.0.0.1:10000/')


"""uvicorn main:app --reload --port 3000"""
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/listado-canciones")
async def get_listado_canciones(request: Request):
    return templates.TemplateResponse("listado_canciones.html", {"request": request, "base_url": BASE_URL})


"""
Estado de Sincronización: Si abres la ventana del reproductor más de una vez y cambias de diapositiva en una, 
no se actualizará automáticamente en las otras ventanas a menos que implementes una forma de sincronización de estado,
 como localStorage, sessionStorage, o WebSockets para mantener las ventanas sincronizadas.
 
Implementar pre-cargar diapositivas o lazy loading para mejorar experiencia de usuario.
Estilos y Pantalla Completa: Para los botones de control de pantalla completa y minimización, 
necesitarás añadir lógica adicional en JavaScript para manejar estos casos. 
Además, para el estilo y la funcionalidad de pantalla completa, 
podrías necesitar algo de CSS adicional y usar la API de pantalla completa de HTML5.
Seguridad: Asegúrate de validar y sanitizar los valores del ID de la canción para prevenir vulnerabilidades de seguridad.
"""


@app.get("/reproductor")
async def get_reproductor(request: Request):
    return templates.TemplateResponse("reproductor.html", {"request": request, "base_url": BASE_URL})
