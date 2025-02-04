print ("calculadora simple")

num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))
if num1 == 5 and num2 == 5:
    print ("suma: es patata")
else:
    resultado = num1 + num2
    print (f"suma: {resultado}")
resultado = num1 - num2
print (f"resta: {resultado}")
resultado = num1 * num2
print (f"multiplicación: {resultado}")
resultado = num1 / num2
print (f"división: {resultado}")

#las variables num y resultado son para darles un valor numerico que nosotros queramos
#float es para ingresar numeros flotantes (osea como 2.0 o 2.5, etc)
#input es para escribir algo en la terminal de la computadora
#if hara la accion que le pidamos si lo que pongamos sea verdadero, si es falso no lo hara
#else hara la accion que le pidamos si la accione en if es falsa
