# implementar y operar con matrices

import random

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz1 = []
print("\nIngrese los valores para la primera matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Valor para posición ({i+1},{j+1}): "))
        fila.append(valor)
    matriz1.append(fila)

matriz2 = []
print("\nIngrese los valores para la segunda matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Valor para posición ({i+1},{j+1}): "))
        fila.append(valor)
    matriz2.append(fila)

print("\nPrimera Matriz:")
for fila in matriz1:
    print(fila)

print("\nSegunda Matriz:")
for fila in matriz2:
    print(fila)

print("\nSuma de las matrices:")
for i in range(filas):
    fila_suma = []
    for j in range(columnas):
        fila_suma.append(matriz1[i][j] + matriz2[i][j])
    print(fila_suma)

print("\nResta de las matrices:")
for i in range(filas):
    fila_resta = []
    for j in range(columnas):
        fila_resta.append(matriz1[i][j] - matriz2[i][j])
    print(fila_resta)

if columnas == filas:  
    print("\nMultiplicación de las matrices:")
    for i in range(filas):
        fila_producto = []
        for j in range(columnas):
            suma = 0
            for k in range(columnas):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_producto.append(suma)
        print(fila_producto)
else:
    print("\nNo se pueden multiplicar las matrices: dimensiones incompatibles.")
