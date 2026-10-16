import json

def obtener_aulas():
    with open("data/aulas.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)