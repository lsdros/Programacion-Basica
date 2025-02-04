print ("factorial de un numero")

num = int(input("ingresa un numero: "))

cont = num
lol = num

while (cont > 1):
    num = num * (cont - 1)
    cont = cont - 1
print (f"factorial de {lol}: {num}") 

#while hara una accion escrita cuando lo que escribamos sea verdadero y terminara la accion cuando este deje de ser verdadero