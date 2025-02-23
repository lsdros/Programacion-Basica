# crear un conversor de unidades

print("\n--- Conversor de Unidades ---")

while True:
    print("\nSeleccione la conversión:")
    print("1. Longitud (metros <-> kilómetros)")
    print("2. Masa (kilogramos <-> gramos)")
    print("3. Temperatura (Celsius <-> Fahrenheit)")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == '1':
        print("\nLongitud:")
        print("a. Metros a kilómetros")
        print("b. Kilómetros a metros")
        sub_opcion = input("Seleccione una opción (a/b): ")

        valor = float(input("Ingrese el valor a convertir: "))
        if sub_opcion == 'a':
            resultado = valor / 1000
            print(f"{valor} metros = {resultado} kilómetros")
        elif sub_opcion == 'b':
            resultado = valor * 1000
            print(f"{valor} kilómetros = {resultado} metros")
        else:
            print("Opción no válida.")

    elif opcion == '2':
        print("\nMasa:")
        print("a. Kilogramos a gramos")
        print("b. Gramos a kilogramos")
        sub_opcion = input("Seleccione una opción (a/b): ")

        valor = float(input("Ingrese el valor a convertir: "))
        if sub_opcion == 'a':
            resultado = valor * 1000
            print(f"{valor} kg = {resultado} g")
        elif sub_opcion == 'b':
            resultado = valor / 1000
            print(f"{valor} g = {resultado} kg")
        else:
            print("Opción no válida.")

    elif opcion == '3':
        print("\nTemperatura:")
        print("a. Celsius a Fahrenheit")
        print("b. Fahrenheit a Celsius")
        sub_opcion = input("Seleccione una opción (a/b): ")

        valor = float(input("Ingrese la temperatura a convertir: "))
        if sub_opcion == 'a':
            resultado = (valor * 9/5) + 32
            print(f"{valor} °C = {resultado} °F")
        elif sub_opcion == 'b':
            resultado = (valor - 32) * 5/9
            print(f"{valor} °F = {resultado} °C")
        else:
            print("Opción no válida.")

    elif opcion == '4':
        print("Saliendo del conversor. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
