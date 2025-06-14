# app/auth.py

from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException

SECRET_KEY = "clave_secreta_super_segura"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30

def crear_token(data: dict):
    datos_a_codificar = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    datos_a_codificar.update({"exp": expire})
    return jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
