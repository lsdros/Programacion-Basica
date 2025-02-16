#leer, escribir y modificar un archivo de texto

def leer_archivo(nombre):
    """Lee y muestra el contenido del archivo."""
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            print("\n Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(" El archivo no existe.")

def escribir_archivo(nombre):
    """Sobrescribe el archivo con un nuevo contenido."""
    nuevo_contenido = input(" Escribe el nuevo contenido: ")
    with open(nombre, "w") as archivo:
        archivo.write(nuevo_contenido + "\n")
    print(" Se ha sobrescrito el archivo.")

def agregar_archivo(nombre):
    """Agrega contenido al final del archivo."""
    nuevo_contenido = input(" Escribe el texto a agregar: ")
    with open(nombre, "a") as archivo:
        archivo.write(nuevo_contenido + "\n")
    print(" Se ha agregado el texto al archivo.")

def modificar_archivo(nombre):
    """Modifica un archivo reemplazando una palabra."""
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
        
        print("\n Contenido actual:")
        print(contenido)
        
        palabra_antigua = input(" Palabra a reemplazar: ")
        palabra_nueva = input(" Nueva palabra: ")

        contenido_modificado = contenido.replace(palabra_antigua, palabra_nueva)

        with open(nombre, "w") as archivo:
            archivo.write(contenido_modificado)
        
        print(" El archivo ha sido modificado.")
    
    except FileNotFoundError:
        print(" El archivo no existe.")

def menu():
    nombre_archivo = "archivo.txt"

    while True:
        print("\n MENÚ:")
        print("1️ Leer archivo")
        print("2️ Escribir (sobrescribir) archivo")
        print("3️ Agregar texto al archivo")
        print("4️ Modificar archivo")
        print("5️ Salir")

        opcion = input(" Elige una opción: ")

        if opcion == "1":
            leer_archivo(nombre_archivo)
        elif opcion == "2":
            escribir_archivo(nombre_archivo)
        elif opcion == "3":
            agregar_archivo(nombre_archivo)
        elif opcion == "4":
            modificar_archivo(nombre_archivo)
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción no válida. Inténtalo de nuevo.")

menu()
