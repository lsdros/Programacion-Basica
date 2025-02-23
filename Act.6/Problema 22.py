# simular el lanzamiento de un dado y una moneda

import random

yn = "y"

while yn == input("¿desea tirar una moneda y lanzar un dado? \ny/n: "):

    print(f"lanzamiento del dado: {random.randint (1, 6)}")

    print(f"Lanzamiento de la moneda: {random.choice(['Cara', 'Cruz'])}")