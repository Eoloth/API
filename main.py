from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
import re

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "!Bienvenido a tu primera API con FastAPI!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje:" f"Hola, {nombre}. Bienvenido a FastApi 👋"}

# Modelo de datos
class Usuario(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    edad: int = Field(..., gt=0, description="Debe ser mayor que 0")

@app.post("/registro")
def registrar_usuario(usuario: Usuario):
    if not re.fullmatch(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", usuario.nombre):
        raise HTTPException(
            status_code=400,
            detail="El nombre solo puede contener letras y espacios (sin números ni símbolos)."
        )

    return JSONResponse(
        status_code=201,
        content={
            "mensaje": f"Usuario {usuario.nombre} de {usuario.edad} años registrado correctamente."
        }
    )
