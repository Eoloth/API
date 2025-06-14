# app/models/user.py

from pydantic import BaseModel, Field

class Usuario(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    edad: int = Field(..., gt=0, description="Debe ser mayor que 0")

class Credenciales(BaseModel):
    username: str
    password: str
