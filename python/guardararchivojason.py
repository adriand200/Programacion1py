#guardar archivo en formato json
import json
datos = {
        "nombre":"carlos",
        "apellido":"gonzales",
        "gmail":"asdfds@gmail.com",
        "telefono":"1234"
        },
#guardar
archivo = open("informacion.json", "w")#abrir el archivo en modo escritura
json.dump(datos, archivo)#guardar el archivo en formato json
archivo.close()#cerrar el archivo