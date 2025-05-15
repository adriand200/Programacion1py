import math
base=float(input("ingreese la base del terreno: "))
altura=float(input("ingreese la altura del terreno: "))
alturarec=float(input("ingreese la altura del terreno-rectangulo: "))
triangulo =(base*altura)/2
rectangulo=(base*alturarec)
areatotal=triangulo+rectangulo
print(f"El área total del terreno es: {areatotal} m²")