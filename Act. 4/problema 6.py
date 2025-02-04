print ("calcular el interes compuesto dado un capital, tasa y tiempo")

capital = float(input("ingrese la capital inicial: "))
tasa = float(input("ingrese la tasa de interés: "))
tiempo = float(input("ingrese periodo del ahorro: "))

capfinal = capital * (1 + tasa) ** tiempo
print (f"el interes compuesto es {capfinal}:")