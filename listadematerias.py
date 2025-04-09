# Este programa permite ingresar el nombre y la nota de varias materias
lista = []
materias = int(input("Ingrese el número de materias que está viendo: "))

for i in range(materias):
    materia = input(f"Ingrese el nombre de la materia {i + 1}: ")
    nota = input(f"Ingrese la nota de la materia {i + 1}: ")
    lista.append((materia, nota))

print("Lista de materias y notas:")
print(lista)