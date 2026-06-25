
matriz = []
numero = 1

for i in range(4):
    fila = []
    for j in range(4):
        fila.append(numero)
        numero += 1
    matriz.append(fila)

print("Matriz 4x4:")
for fila in matriz:
    print(fila)

suma_diagonal = 0
multiplicacion_diagonal = 1

for i in range(4):
    suma_diagonal += matriz[i][i]
    multiplicacion_diagonal *= matriz[i][i]

print("\nElementos de la diagonal principal:")
for i in range(4):
    print(matriz[i][i], end=" ")

print("\n\nSuma de la diagonal principal:", suma_diagonal)
print("Multiplicación de la diagonal principal:", multiplicacion_diagonal)