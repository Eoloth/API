import requests
from fastapi import HTTPException

def obtener_pokemon_info(nombre: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")

    data = respuesta.json()
    
    return {
        "nombre": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "habilidades": [h["ability"]["name"] for h in data["abilities"]],
        "imagen_url": data["sprites"]["front_default"]
    }
