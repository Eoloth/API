from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models import Usuario
from app.utils import obtener_pokemon_info
import re

router = APIRouter()

@router.get("/")
def root():
    return {"mensaje": "¡Bienvenido a tu primera API con FastAPI!"}

@router.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}. Bienvenido a FastAPI 👋"}

@router.post("/registro")
def registrar_usuario(usuario: Usuario):
    if not re.fullmatch(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", usuario.nombre):
        raise HTTPException(status_code=400, detail="El nombre solo puede contener letras y espacios.")
    return JSONResponse(status_code=201, content={"mensaje": f"Usuario {usuario.nombre} de {usuario.edad} años registrado correctamente."})

@router.get("/pokemon/{nombre}")
def get_pokemon(nombre: str):
    return obtener_pokemon_info(nombre)
