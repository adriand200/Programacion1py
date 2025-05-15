def mensaje ():

    print("unisangil")
mensaje()

def suma (a,b):
    """
    suma 2 numeros:int a + b
    """
    rta = a+b
    print(rta)
suma(10,5)
def multiplicacion (a,b):
    """
    multiplicacion 2 numeros:int a * b
    """
    rta = a*b
    return rta
rta=multiplicacion(10,5)
print(rta)
#funcion simple con valor de retorno 
def solicitar_datos ():
    """
    Solicita al usuario un numero y lo retorna
    """
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese un numero: "))
    return num1, num2
a,b=solicitar_datos()
print(f"primer numero: {a} y segundo numero {b}")    