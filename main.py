from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "!Bienvenido a tu primera API con FastAPI!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje:" f"Hola, {nombre}. Bienvenido a FastApi 👋"}

from pydantic import BaseModel

# Modelo de datos
class Usuario(BaseModel):
    nombre: str
    edad: int

@app.post("/registro")
def registrar_usuario(usuario: Usuario):
    return {
        "mensaje": f"Usuario {usuario.nombre} de {usuario.edad} años registrado correctamente."
    }
