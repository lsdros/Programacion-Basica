#Implementar busqueda binaria y lineal

def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en una lista no ordenada.
    Devuelve el índice del elemento si se encuentra, sino -1.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    Devuelve el índice del elemento si se encuentra, sino -1.
    """
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda
