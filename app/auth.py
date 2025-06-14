from datetime import datetime, timedelta
from jose import JWTError, jwt

# Clave secreta para firmar el token
SECRET_KEY = "clave_secreta_super_segura"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30

def crear_token(datos: dict):
    datos_a_codificar = datos.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    datos_a_codificar.update({"exp": expiracion})
    token = jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
