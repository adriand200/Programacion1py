import json
import datetime

archivo = open("informacion.json", "r")

contenido = json.load(archivo)

datos = json
archivo.close()#cerrar el archivo

usernama = input("ingrese el nuevo nombre de usuario: ")
contenido["nombre"] = usernama
contenido["fecha_modificacion"] = str(datetime.datetime.now())

archivo = open("datos.json,new", "w")#abrir el archivo en modo escritura
json.dump(datos, archivo)#guardar el archivo en formato json
archivo.close()#cerrar el archivo