programacion={"docente":
            {"nombre":"carlos",
                        "apellido":"gonzales",
                        "gmail":"asdfds@gmail.com",
                        "telefono":"1234"},
            "estudiantes":[
                {
                    "nombre":"juanito",
                    "apellido":"rodriguez",
                    "cc":"12388",
                    "correo":"furnef@gmail.com"
                },
                {
                    "nombre":"juan",
                    "apellido":"rodriguez",
                    "cc":"12356",
                    "correo":"furnrgerf@gmail.com"
                },
                {
                    "nombre":"pepito",
                    "apellido":"rondano",
                    "cc":"14556",
                    "correo":"fregthf@gmail.com"
                },
                {
                    "nombre":"juanillo",
                    "apellido":"perez",
                    "cc":"128465",
                    "correo":"ehtf@gmail.com"
                }
            ],
            "codigo":"123456",
            "estado":"True",
            "creditos":3,}
print(type(programacion))
print(programacion["docente"])
print(programacion["docente"]["nombre"])
print(f"el nombre del docente es",programacion["docente"]["nombre"])
for estudiante in programacion["estudiantes"]:
    print["nombre"]
    print["apellido"]
    print["cc"]
    print["correo"]
print(programacion.items())
print(programacion["docente"].items())#saca duplas 
print(programacion.keys())#saca las llaves
for estudiante in programacion["estudiantes"]:
    print(estudiante.keys())#saca las llaves de los estudiantes
print(programacion.values())#saca los valores
print(programacion["docente"].values())#saca los valores del docente
for estudiante in programacion["estudiantes"]:
    print(estudiante.values())#saca los valores de los estudiantes(estudiantes)
print(programacion.get)
#Cambiar información en el diccionario 
programacion ["docente"]["nombre"] = "Jesus caro"
#agregar atributo 
programacion ["programa"]="ingeniería de sistemas "
#para eliminar un atributo 
