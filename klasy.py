#Klasa = Szablon, Przepis

class Czlowiek:
    #Istota
    gatunek = "Homo sapiens"
    def __init__(self):
        # Konstruktor
        # Akt istnienia
        print("Niech powstanie czlowiek")
        pass

#Powstanie z obiektu
#Gotowanie z przepisu

adam = Czlowiek()
print(adam.gatunek)