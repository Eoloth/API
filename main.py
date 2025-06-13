from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "!Bienvenido a tu primera API con FastAPI!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje:" f"Hola, {nombre}. Bienvenido a FastApi 👋"}