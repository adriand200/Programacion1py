#este programa hace la tabla de multiplicar 
numero=int(input("Ingrese el número para la tabla de multiplicar: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")