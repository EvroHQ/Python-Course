import random

nombre_mystere = random.randint(0, 10)
nombre = input("Quel est le nombre mystère ? ")

if nombre.isdigit():
    nombre = int(nombre)
    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    if nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo! Vous avez trouvé le nombre mystère!")
else:
    print("SVP! Rentrez un nombre valide!")
else:
    print("TG")