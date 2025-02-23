# generar y analizar datos estadisticos

import random
import statistics
import matplotlib.pyplot as plt

# Generar datos aleatorios
cantidad = int(input("Ingrese la cantidad de datos a generar: "))
datos = [random.randint(1, 100) for _ in range(cantidad)]

# Mostrar datos generados
print("\n Datos generados:")
print(datos)

# Calcular estadísticas básicas
media = sum(datos) / cantidad
mediana = statistics.median(datos)
moda = statistics.mode(datos)
varianza = statistics.variance(datos)
desviacion = statistics.stdev(datos)

# Mostrar resultados
print("\n Análisis estadístico:")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")

# Graficar histograma
plt.hist(datos, bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Datos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Media: {media:.2f}')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1.5, label=f'Mediana: {mediana}')
plt.legend()
plt.show()
