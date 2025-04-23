"quiz paneles solaes"
print("bienvenido al programa de calculo de paneles solares en un perimetro dependiendo de la radiacion solar")
import math
consumoenergia=float(input("ingrese el consumo de energia: "))  
horas=float(input("ingrese las horas de sol: "))
eficiencia=float(input("ingrese la eficiencia del panel: "))
eficiencia1=eficiencia/100
anchopane=float(input("ingrese el ancho del panel: "))
largo=float(input("ingrese el largo del panel: "))
area=(anchopane*largo)
print(f"el area del panel es: {area} m²")
radiacionpromedio=float(input("ingrese la radiacion promedio: "))
potenciadia=area*radiacionpromedio*eficiencia1
print(f"la potencia diaria del panel es: {potenciadia} kWh")
potenciaaño= potenciadia*365
print(f"la potencia anual del panel es: {potenciaaño} KWh")
numeropaneles=math.ceil(consumoenergia/potenciaaño)
print(f"el numero de paneles necesarios es de: {numeropaneles}")