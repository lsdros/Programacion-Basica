#Implementer distintos metodos de ordenamiento

import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:  
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i] 
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivote]
        medio = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x > pivote]
        return quick_sort(izquierda) + medio + quick_sort(derecha)

def probar_ordenamientos():
    lista = [random.randint(1, 100) for _ in range(10)]  

    print("\nLista original:", lista)

    print("\n🔹 Bubble Sort:", bubble_sort(lista[:])) 
    print("\n🔹 Selection Sort:", selection_sort(lista[:]))
    print("\n🔹 Insertion Sort:", insertion_sort(lista[:]))
    print("\n🔹 Merge Sort:", merge_sort(lista[:]))
    print("\n🔹 Quick Sort:", quick_sort(lista[:]))

probar_ordenamientos()
