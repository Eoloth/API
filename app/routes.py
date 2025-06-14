from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from app.auth import crear_token
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from app.auth import verificar_token
from fastapi.responses import JSONResponse
from app.models import Usuario
from app.utils import obtener_pokemon_info
import re

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Usuario simulado
usuarios = {
    "admin": pwd_context.hash("admin123")
}
class Credenciales(BaseModel):
    username: str
    password: str

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
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return {"usuario": payload["sub"], "mensaje": "Acceso permitido a la ruta protegida"}

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
