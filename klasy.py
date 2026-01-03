#Klasa = Szablon, Przepis
from tokenize import String


class Czlowiek:
    #Istota
    #Atrybuty klasy
    gatunek = "Homo sapiens"
    def __init__(self, imie, plec): #Atrybuty OOBIEKTU (skladniki potrawy)
        # Konstruktor
        # Akt istnienia
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec
        #adam.imie = "Adam"
        #ewa.imie = "Ewa"

    #Metoda
    #Moznosc (mozliwosc), zdolnosc, umiejetnosc
    def przedstaw_sie(self):
        print(f"Dzien dobry, am na imie {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("mezczyzna")
        else:
            print("kobieta")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa, juhuu!!!")

    def przedstaw_sie(self):
        print(f"Cesc, mam na imie {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("chlopcem")
        else:
            print("dziewcynka")


#Powstanie z obiektu
#Gotowanie z przepisu

adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")
kain = Dziecko("Kain", "M")

print(adam.gatunek)
print(ewa.gatunek)

adam.przedstaw_sie()
ewa.przedstaw(adam)
kain.baw_sie()
kain.przedstaw_sie()