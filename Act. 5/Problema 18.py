#Resolver ecuaciones cuadraticas

import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f" Dos soluciones reales: x1 = {x1}, x2 = {x2}"
    
    elif discriminante == 0:
        x = -b / (2 * a)
        return f" Una única solución real: x = {x}"
    
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * a)
        return f" Soluciones complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print(" No es una ecuación cuadrática (a no puede ser 0).")
else:
    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print("\n Resultado:", resultado)

