import random

user_number = random.randint(0, 10)
number = input("Devinez un chiffre de 0 à 10: ")

if number.isdigit():
    number = int(number)
    if number > user_number:
        print(f"Le chiffre est plus petit que {number}")
    elif number < user_number:
        print(f"Le chiffre est plus grand que {number}")
    else:
        print("Bravo vous avez trouver le chiffre mystère !")
else:
    print("SVP! Entrez un chiffre valide!")