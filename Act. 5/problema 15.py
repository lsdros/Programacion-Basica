#Determinar si un año es bisiestro

año = int(input("Ingresa un año: "))

if año % 4 == 0:
    print (f"el año {año} es bisiesto")
elif (año % 100) % 400 == 0:
    print (f"el año {año} es bisiesto")
else:
    print (f"el año {año} no es bisiesto")