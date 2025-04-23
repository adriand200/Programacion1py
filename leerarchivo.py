
import json
archivo = open("imformacion.json", "r")

contenido = json.load(archivo)
print(contenido)
archivo.close()#cerrar el archivo