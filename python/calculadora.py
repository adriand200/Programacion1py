# calculadora
import math
while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")
    
    opcion = int(input("Ingrese una opción: "))

    if opcion == 7:
        print("Gracias por usar la calculadora")
        break
    elif opcion == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        suma = a + b
        print(f"La suma de los números es: {suma}")
    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resta = a - b
        print(f"La resta de los números es: {resta}")
    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        multiplicacion = a * b
        print(f"La multiplicación de los números es: {multiplicacion}")
    elif opcion == 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            division = a / b
            print(f"La división de los números es: {division}")
    elif opcion == 5:
        a = float(input("Ingrese el número base: "))
        b = float(input("Ingrese el exponente: "))
        potencia = math.pow(a, b)
        print(f"La potencia de los números es: {potencia}")
