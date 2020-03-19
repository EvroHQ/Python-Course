import os
import random

directory = r"D:\structure_dossier"

d = {"film": ["Harry Potter",
            "Bloom",
            "Titanic"],
    "Dates": ["12-02-2020"]}

for key, value in d.items():
    for dossier in value:
        chemin_dossier = os.path.join(directory, key, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)