from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Pokémon API + Registro de Usuarios")

app.include_router(router)
