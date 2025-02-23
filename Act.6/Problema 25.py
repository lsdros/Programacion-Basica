#generar y analizar histogramas de datos

import matplotlib.pyplot as plt
import random

# Generar datos aleatorios
cantidad_datos = int(input("Ingrese la cantidad de datos a generar: "))
datos = [random.randint(1, 100) for _ in range(cantidad_datos)]

print("\nDatos generados:")
print(datos)

media = sum(datos) / cantidad_datos
datos_ordenados = sorted(datos)
mediana = datos_ordenados[cantidad_datos // 2] if cantidad_datos % 2 != 0 else \
    (datos_ordenados[cantidad_datos // 2 - 1] + datos_ordenados[cantidad_datos // 2]) / 2
moda = max(set(datos), key=datos.count)

print(f"\nEstadísticas:")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

plt.hist(datos, bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Datos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Media: {media:.2f}')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1, label=f'Mediana: {mediana:.2f}')
plt.legend()
plt.show()
