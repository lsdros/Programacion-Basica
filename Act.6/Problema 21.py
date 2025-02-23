#Calcular el área y volumen de distintas figuras geometricas

import math

medida = int(input("¿Ingrese que desea saber? \n1 -Area \n2 -Volumen \n"))
if medida == 1:
    forma_2_dimensiones = int(input("¿Ingrese que forma geoemtrica desea saber su area? \n1 -Cuadrado \n2 -triangulo \n3 -rectangulo \n4 -circulo \n"))
    if forma_2_dimensiones == 1:
        lado = float(input("Ingrese la medida de un lado: "))
        area = lado ** 2
        print(f"el area del cuadrado es {area}")
    elif forma_2_dimensiones == 2:
        altura = float(input("ingrese la altura del triangulo: "))
        base = float(input("ingrese la base del triangulo: "))
        area = (altura * base)/ 2
        print(f"el area del triangulo es {area}")
    elif forma_2_dimensiones == 3:
        altura = float(input("ingrese la altura del rectangulo: "))
        base = float(input("ingrese la base del rectangulo: "))
        area = (altura * base)
        print(f"el area del rectangulo es {area}")
    else:
        radio = float(input("ingrese el radio del circulo: "))
        area = math.pi * radio**2
        print (f"el area del circulo es {area}")
else:
    forma_3_dimensiones = int(input("¿Ingrese que forma geometrica desea saber su volumen? \n1 -cubo \n2 -piramide \n3 -prisma rectangular \n4 -esfera \n"))
    if forma_3_dimensiones == 1:
        lado = float(input("ingrese la medida de un lado: "))
        volumen = lado ** 3
        print(f"el volumen del cuadrado es {volumen}")
    elif forma_3_dimensiones == 2:
        lado_1 = float(input("ingrese la medida de un lado de la base: "))
        lado_2 = float(input("ingrese la medida de otro lado de la base: "))
        area_base = lado_1 * lado_2
        altura = float(input("ingrese la altura del piramide: "))
        volumen = (area_base * altura) / 3
        print(f"el volumen del piramide es {volumen}")
    elif forma_3_dimensiones == 3:
        longitud = float(input("ingrese la longitud: "))
        anchura = float(input("ingrese la anchura: "))
        altura = float(input("ingre la altura: "))
        volumen = longitud*anchura*altura
        print(f"el volumen del primsa rectangular {volumen}")
    else:
        radio = float(input("ingrese el radio: "))
        volumen = 4/3 (math.pi * radio ** 3)
        print(f"el volumen del esfera {volumen}")
