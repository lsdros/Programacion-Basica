# implementar una agenda de contacto

agenda = {}

while True:
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        email = input("Ingrese el correo electrónico: ")
        agenda[nombre] = {"Teléfono": telefono, "Email": email}
        print(f"Contacto '{nombre}' agregado con éxito.")

    elif opcion == '2':
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Contacto: {nombre}")
            print(f"Teléfono: {agenda[nombre]['Teléfono']}")
            print(f"Email: {agenda[nombre]['Email']}")
        else:
            print("Contacto no encontrado.")

    elif opcion == '3':
        if agenda:
            print("\nLista de contactos:")
            for nombre, info in agenda.items():
                print(f"- {nombre}: Teléfono: {info['Teléfono']}, Email: {info['Email']}")
        else:
            print("La agenda está vacía.")

    elif opcion == '4':
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto '{nombre}' eliminado.")
        else:
            print("Contacto no encontrado.")

    elif opcion == '5':
        print("Saliendo de la agenda. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
