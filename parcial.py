# Este programa simula el sistema de un cajero
import math
intel = 3
contraseña1 = 1234
saldo = 1000
while True:
    contraseña = int(input("Ingrese su contraseña: "))
    if contraseña == contraseña1:
        while True:
            print("1. Consultar saldo")
            print("2. Realizar un depósito")
            print("3. Realizar un retiro")
            print("4. Salir")
            opcion = int(input("Ingrese una opción: "))
            if opcion == 4:
                break
            elif opcion == 1:
                saldo+deposito
                saldo-retiro
                print(f"Su saldo es:",saldo)
            elif opcion == 2:
                deposito = int(input("Cuánto desea depositar "))
                saldo += deposito
                print("Depósito realizado")
                print(f"Su saldo es:",saldo)
            elif opcion == 3:
                retiro = int(input("¿Cuánto desea retirar? "))
                if saldo > retiro:
                    print("Su retiro fue exitoso")
                else:
                    print("Fondos insuficientes")
        break
    else:
        intel -= 1
        print(f"Contraseña incorrecta, le quedan",intel, "intentos")
        if intel < 1:
            print("se a queado sin intentos")
            break