# Definir una matriz
matriz_a = [
    [1, 2, 3],
    [0, 5, 4],
]

# Imprimir la matriz
print(f"Matriz A: {matriz_a}")

# Sacar los datos por posición
print(matriz_a[0][0])  # 1
print(matriz_a[1][1])  # 5
print(matriz_a[0][2])  # 3

# Tamaño de la matriz
longitud = len(matriz_a)  # Número de filas
print(f"Longitud de la matriz (filas): {longitud}")
ancho = len(matriz_a[0])  # Número de columnas
print(f"Ancho de la matriz (columnas): {ancho}")

# Imprimir los datos de la matriz con sus posiciones
for i in range(longitud):
    for j in range(ancho):
        print(f"Posición: ({i}, {j}) = {matriz_a[i][j]}")

# Importar NumPy
import numpy as np

# Crear una matriz con NumPy
matriz_B = np.array([[1, 2, 3], [0, 5, 4]])
print(f"Matriz B:\n{matriz_B}")

# Convertir matriz_a a un array de NumPy para realizar operaciones
matriz_a_np = np.array(matriz_a)

# Suma de matrices
matriz_suma = matriz_a_np + matriz_B
print(f"Matriz suma:\n{matriz_suma}")

# Resta de matrices
matriz_resta = matriz_a_np - matriz_B
print(f"Matriz resta:\n{matriz_resta}")
#como extraer parametros de la matriz
print(type(matriz_a_np))  # <classe
print(f"filas x columnas: {matriz_a_np.shape}")# (filas, columnas)
print(f"# de datos: {matriz_a_np.size}")# # de datos
print(f"tipo de datos: {matriz_a_np.dtype}")# tipo de datos internos
print(f"numero de dimensiones: {matriz_a_np.ndim}")# numero de dimensiones