#Verficar si una cadena es un palindromo

cadena = input("Ingrese una cadena de caracteres: ")

cadena_corta = cadena.lower().replace(" ", "")
if cadena_corta == cadena_corta [::-1]:
    print(f"{cadena} es un palindromo")
else:
    print (f"{cadena} no es un palindromo")

#Usar .lower hace que la palabra que se le de a la computadora sea en minusculas
#Usar .replace hace que quite los espacion de la palabra escrita
#Usar [::-1] hace que tu palabra se volte o cualquier cosa dada