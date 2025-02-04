print ("verificar si un numero es primo")

num = int(input("ingresa un numero: "))

final = 2
ver = False
primo = False

while ((final < num) and (primo == False)):
    ver = (num % final == 0)
    final = final + 1
    if (ver == True):
        print ("no es primo")
        primo = True

if (primo == False):
    print ("primo")