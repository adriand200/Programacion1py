#tablero de ajedrez 8*8
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
logitud= len(tablero)
# Imprimir el tablero con sus posiciones
for i in range(logitud):
    for j in range(logitud ):
        
