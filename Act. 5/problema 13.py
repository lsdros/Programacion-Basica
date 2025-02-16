#convertir una temperatura entre distintas escalas
yn = "y"

while yn == "y":
    temperatura = float(input("Ingrese una temperatura a convertir: "))
    selec = int(input(f"Ingrese la escala de su temperatura: \n1 - Celsius \n2 - Fahrenheit \n3 - Kelvin \n "))
    cond = int(input(f"Ingrese la escala a convertir: \n1 - Celsius \n2- Fahrenheit \n3 - Kelvin \n "))
    if (selec == 1):
        if(cond == 1):
            print(temperatura)
        elif (cond == 2):
            print((9*temperatura)/5+32)
        else:
            print(temperatura+273.15)
    elif (selec == 2):
        if(cond == 1):
            print(5*(temperatura-32)/9)
        elif (cond == 2):
            print(temperatura)
        else:
            print(5*(temperatura-32)/9+273.15)
    else:
        if(cond == 1):
            print(temperatura-273.15)
        elif(cond == 2):
            print(9*(temperatura-273.15)/5+32)
        else:
            print(temperatura)
    yn = input("¿Deseas realizar otra operación? y/n: ")