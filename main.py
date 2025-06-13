from fastapi import FastAPI
from pydantic import BaseModel, Field
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
    if not usuario.nombre.isalpha():
        raite HTTPExecption(
            status_code = 400, 
            detail="El nombre solo debe contener ltras (sin espacios, números o símbolos".
            )
    return {
        "mensaje": f"Usuario {usuario.nombre} de {usuario.edad} años registrado correctamente."
    }