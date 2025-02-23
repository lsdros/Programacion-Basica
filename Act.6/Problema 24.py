# calcular la suma de una serie numérica

print("Seleccione el tipo de serie:")
print("1. Serie aritmética (a, a+d, a+2d, ...)")
print("2. Serie geométrica (a, a*r, a*r², ...)")
opcion = int(input("Ingrese 1 o 2: "))

n = int(input("\nIngrese la cantidad de términos (n): "))
suma = 0

if opcion == 1:
    a = float(input("Ingrese el primer término (a): "))
    d = float(input("Ingrese la diferencia común (d): "))

    suma = n * (2 * a + (n - 1) * d) / 2

    print("\nSerie aritmética:")
    for i in range(n):
        print(a + i * d, end=" ")
    print(f"\nSuma de la serie: {suma}")

elif opcion == 2:
    a = float(input("Ingrese el primer término (a): "))
    r = float(input("Ingrese la razón común (r): "))

    if r == 1:
        suma = a * n
    else:
        suma = a * (1 - r**n) / (1 - r)

    print("\nSerie geométrica:")
    for i in range(n):
        print(a * (r ** i), end=" ")
    print(f"\nSuma de la serie: {suma}")

else:
    print("Opción no válida.")
