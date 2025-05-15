# Importar funciones desde los scripts
from interfaz import (
    menu,
    solicitar_datos_cuadrado,
    solicitar_datos_circulo,
    solicitar_datos_triangulo,
    mostrar_area_cuadrado,
    mostrar_area_circulo,
    mostrar_area_triangulo
)
from figuras import (
    area_cuadrado,
    area_circulo,
    area_triangulo
)

# Constantes para las opciones del menú
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
SALIR = 4

# Inicializar la variable de opción
op = 0

# Bucle principal
while op != SALIR:
    # Mostrar el menú y leer la opción del usuario
    op = menu()

    # Procesar la opción seleccionada
    if op == CUADRADO:
        lado = solicitar_datos_cuadrado()
        area = area_cuadrado(lado)
        mostrar_area_cuadrado(area)

    elif op == CIRCULO:
        radio = solicitar_datos_circulo()
        area = area_circulo(radio)
        mostrar_area_circulo(area)

    elif op == TRIANGULO:
        base, altura = solicitar_datos_triangulo()
        area = area_triangulo(base, altura)
        mostrar_area_triangulo(area)

    elif op == SALIR:
        print("¡Gracias por utilizar la calculadora de figuras geométricas!")

    else:
        print("¡Opción no válida! Por favor, intenta de nuevo.")
