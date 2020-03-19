import os
import json


dossier_courant = r"D:/liste_courses"
chemin_liste = os.path.join(dossier_courant, "liste.json")

if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)

else:
    liste_de_courses = []

affichage = """
Selectionner une option:
\t1. Ajouter un élément.
\t2. Effacer un élément.
\t3. Afficher la liste.
\t4. Supprimer la liste.
\t5. Quitter.
"""

option = "0"

while option != "5":
    option = input(affichage)
    if option == "1":
        add_product = input("Entrez le produit a ajouter: ")
        if add_product.isdigit():
            print("SVP! Entrez un produit valide.")
        else:
            liste_de_courses.append(add_product)
        with open(chemin_liste, "w") as f:
            json.dump(liste_de_courses, f, indent=4)
    elif option == "2":
        remove_product = input("Entrez le produit a supprimer: ")
        liste_de_courses.remove(remove_product)
        with open(chemin_liste, "w") as f:
            json.dump(liste_de_courses, f, indent=4)
    elif option == "3":
        print("\n".join(liste_de_courses))
    elif option == "4":
        del_liste = input("Etes-vous sur ? Répondez par oui ou par non: ")
        if del_liste == "oui":
            liste_de_courses.clear()
        else:
            print("La liste n'a pas été supprimer.")
        with open(chemin_liste, "w") as f:
            json.dump(liste_de_courses, f, indent=4)  