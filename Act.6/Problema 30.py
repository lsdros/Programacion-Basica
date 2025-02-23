#Implementar funciones recursivas

factorial = (lambda n: 1 if n == 0 else n * factorial(n - 1))

fibonacci = (lambda n: 0 if n == 0 else (1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)))

suma_lista = (lambda lista: 0 if not lista else lista[0] + suma_lista(lista[1:]))

potencia = (lambda x, n: 1 if n == 0 else x * potencia(x, n - 1))

print("Factorial de 5:", factorial(5))  # Salida: 120
print("Fibonacci de 6:", fibonacci(6))  # Salida: 8
print("Suma de la lista [1, 2, 3, 4, 5]:", suma_lista([1, 2, 3, 4, 5]))  # Salida: 15
print("2 elevado a 3:", potencia(2, 3))  # Salida: 8