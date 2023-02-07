# evidence pojištěnců (pojištěných)
# umožňuje vytvoření pojištěného
# umožňuje zobrazení seznamu všech pojištěných
# umožňuje vyhledání pojištěného podle jména a příjmení

from pojisteny import Pojisteny


class Evidence_pojistenych:
    def __init__(self):
        self.kartoteka_pojistencu = []



    def vytvoreni_pojisteneho(self):  # založení pojištěnce
        jmeno = input("Zadej jméno pojištěného:")
        prijmeni = input("Zadej příjmení pojištěného:")
        vek = int(input("Zadej věk pojištěného:"))
        telefon = int(input("Zadej mobilní telefonní číslo pojištěného:"))
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.kartoteka_pojistencu.append(novy_pojisteny)


    def vypsat_vsechny_pojistene(self):  # výpis všech uložených pojištěnců
        print(f"Máme v kartotéce {len(self.kartoteka_pojistencu)} pojištěnců a jsou to tito:\n")
        for karta in self.kartoteka_pojistencu:
                print(karta)

    def vyhledat_pojisteneho(self): #vyhledávání pojistěného podle zadání jména a příjmení
        hledat_jmeno = input("Zadej jméno hledaného pojištěného:")
        hledat_prijmeni = input("Zadej příjmení hledaného pojištěného:")
        for karta in self.kartoteka_pojistencu:
            if karta.jmeno == hledat_jmeno and karta.prijmeni == hledat_prijmeni:
                print(f"Vyhledaný pojištěný:\n{(karta)}")
            else:
                print("Bohužel. Hledaného pojištěného v kartotéce nemáme!")

