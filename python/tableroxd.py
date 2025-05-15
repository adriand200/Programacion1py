# Crear el tablero de ajedrez como una matriz 8x8 (con 'B' y 'N' para blanco y negro)
tablero = [
    ['B', 'N', 'B', 'N', 'B', 'N', 'B', 'N'],
    ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B'],
    ['B', 'N', 'B', 'N', 'B', 'N', 'B', 'N'],
    ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B'],
    ['B', 'N', 'B', 'N', 'B', 'N', 'B', 'N'],
    ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B'],
    ['B', 'N', 'B', 'N', 'B', 'N', 'B', 'N'],
    ['N', 'B', 'N', 'B', 'N', 'B', 'N', 'B']
]

# Imprimir el tablero sin usar 'end'
for fila in tablero:
    print(" ".join(fila))  # Usamos join para concatenar las casillas con espacio
