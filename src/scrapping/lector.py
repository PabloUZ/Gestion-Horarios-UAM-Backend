import json

class Lector:
    def __init__(self):
        self.carpeta = 'entradas'

    def leer_json(self, nombre):
        with open(f"{self.carpeta}/{nombre}.json", "r", encoding="utf8") as archivo:
            return json.load(archivo)
