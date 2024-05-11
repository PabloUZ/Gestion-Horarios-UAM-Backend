import json

class Escritor:
    def __init__(self):
        self.carpeta = 'salidas'

    def escribir_json(self, nombre_archivo, contenido):
        with open(f'{self.carpeta}/{nombre_archivo}.json', 'w', encoding="utf8") as archivo:
            json.dump(contenido, archivo, ensure_ascii= False, indent= 4)
