# app/routes/routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from app.auth import crear_token, verificar_token
from app.models.user import Usuario, Credenciales
from app.utils import obtener_pokemon_info
from passlib.context import CryptContext
import re

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Simulación de usuarios
usuarios = {
    "admin": pwd_context.hash("admin123")
}

@router.post("/login")
def login(credenciales: Credenciales):
    user = credenciales.username
    password = credenciales.password

    if user not in usuarios or not pwd_context.verify(password, usuarios[user]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = crear_token({"sub": user})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/usuario/protegido")
def ruta_protegida(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    return {"usuario": payload["sub"], "mensaje": "Acceso permitido"}

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
    return JSONResponse(status_code=201, content={"mensaje": f"Usuario {usuario.nombre} registrado correctamente."})

@router.get("/pokemon/{nombre}")
def get_pokemon(nombre: str):
    return obtener_pokemon_info(nombre)
