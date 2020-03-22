class Voiture:
    
    def __init__(self, marque):
        self.marque = marque

voiture_01 = Voiture("Lamborghini")
voiture_02 = Voiture("Porsche")

print(voiture_01.marque)
print(voiture_02.marque)