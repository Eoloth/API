# API FastAPI - Registro de Usuarios y Pokémons

Proyecto personal para practicar FastAPI, validaciones con Pydantic y consumo de APIs externas como PokéAPI.

## Endpoints

- `GET /`: Mensaje de bienvenida
- `GET /saludo/{nombre}`: Devuelve un saludo personalizado
- `POST /registro`: Registra usuario con validación de nombre y edad
- `GET /pokemon/{nombre}`: Devuelve datos de un Pokémon usando la PokéAPI

## Instalación

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
