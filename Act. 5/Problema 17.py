#Implementar estructura de datos basicos: pila, cola y lista enlazada

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print(" La pila está vacía.")
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print(" La pila está vacía.")
    
    def tamano(self):
        return len(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print(" La cola está vacía.")

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            print(" La cola está vacía.")
    
    def tamano(self):
        return len(self.items)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_primer_elemento(self):
        if not self.esta_vacia():
            self.cabeza = self.cabeza.siguiente
        else:
            print(" La lista está vacía.")

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None" if not self.esta_vacia() else "Lista vacía.")


def probar_estructuras():
    print("\n🔹 Probar Pila:")
    pila = Pila()
    pila.apilar(10)
    pila.apilar(20)
    print(f"Desapilar: {pila.desapilar()}") 
    print(f"Ver tope: {pila.ver_tope()}")  
    print(f"Tamaño de pila: {pila.tamano()}")  

    print("\n🔹 Probar Cola:")
    cola = Cola()
    cola.encolar(30)
    cola.encolar(40)
    print(f"Desencolar: {cola.desencolar()}")  
    print(f"Ver frente: {cola.ver_frente()}")  
    print(f"Tamaño de cola: {cola.tamano()}")  

    print("\n🔹 Probar Lista Enlazada:")
    lista = ListaEnlazada()
    lista.insertar_al_principio(5)
    lista.insertar_al_principio(10)
    lista.mostrar_lista() 
    lista.eliminar_primer_elemento()
    lista.mostrar_lista() 


probar_estructuras()
