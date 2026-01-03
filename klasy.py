#Klasa = Szablon, Przepis
from tokenize import String


class Czlowiek:
    #Istota
    gatunek = "Homo sapiens"
    def __init__(self, imie):
        # Konstruktor
        # Akt istnienia
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie
        #adam.imie = "Adam"
        #ewa.imie = "Ewa"

#Powstanie z obiektu
#Gotowanie z przepisu

adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
print(adam.gatunek)
print(ewa.gatunek)
