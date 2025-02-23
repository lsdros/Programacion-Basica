# simular una cuenta bancaria con depositos y retiros

# Saldo inicial
saldo = 0.0

print("\n--- Simulador de Cuenta Bancaria ---")

while True:
    print("\nSeleccione una opción:")
    print("1. Consultar saldo")
    print("2. Realizar depósito")
    print("3. Realizar retiro")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == '1':
        print(f"Saldo actual: ${saldo:.2f}")

    elif opcion == '2':
        deposito = float(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("El monto debe ser positivo.")

    elif opcion == '3':
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto debe ser positivo.")

    elif opcion == '4':
        print("Gracias por usar el simulador. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
