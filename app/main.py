# app/main.py

from fastapi import FastAPI
from app.routes.routes import router

app = FastAPI(
    title="API de Rubén Manríquez",
    description="Proyecto de aprendizaje con FastAPI, integrando validaciones, rutas y APIs externas.",
    version="1.0.0",
    contact={
        "name": "Rubén Manríquez",
        "url": "https://rubenmanriquez.github.io",
        "email": "ruben.msalles@gmail.com"
    },
    )

app.include_router(router)
