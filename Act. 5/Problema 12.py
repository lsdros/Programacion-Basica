#comprobar cual es el mayor de tres numeros
num1 = int(input("ingrese su primer numero: "))
num2 = int(input("ingrese su segundo numero: "))
num3 = int(input("ingrese su tercer numero: "))

if num1 > num2 and num1 > num3:
    print (f"{num1} es el numero mayor")
elif num2 > num1 and num2 > num3:
    print (f"{num2} es el numero mayor")
else:
    print (f"{num3} es el numero mayor")
    