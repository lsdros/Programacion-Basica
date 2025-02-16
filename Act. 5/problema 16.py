#Contar el numero de vocales y consonantes en una cadena

def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vocales = 0
    num_consonantes = 0

    for letra in cadena:
        if letra in vocales:
            num_vocales += 1
        elif letra in consonantes:
            num_consonantes += 1

    return num_vocales, num_consonantes

cadena = input("Ingrese una cadena: ")

vocales, consonantes = contar_vocales_consonantes(cadena)

print(f"\n Número de vocales: {vocales}")
print(f" Número de consonantes: {consonantes}")
