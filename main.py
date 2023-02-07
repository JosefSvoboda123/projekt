# hlavní kód

from evidencePojistenych import Evidence_pojistenych

kartoteka = Evidence_pojistenych()

for i in range(40):
    print("*", end="")
print()
print("Vítá Vás aplikace Kartotéka pojištěnců")
for i in range(40):
    print("=", end="")
print()

pokracovat = True
while pokracovat:

    print("Máte následující možnosti výběru akce:\n")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    akce = int(input("*** Jaký je Váš výběr akce?:"))

    if akce == 1:
        kartoteka.vytvoreni_pojisteneho() #vytvoření nového pojištěnce

    elif akce == 2:
        kartoteka.vypsat_vsechny_pojistene() #vypsání všech uložených pojištěnců se všemi záznamy

    elif akce == 3:
        kartoteka.vyhledat_pojisteneho()  # vyhledání pojištěného

    elif akce == 4:  # ukončení aplikace
        pokracovat = False
        input("\nProgram ukončíte stiskem klávesy Enter...")

    else:
        print("Chybná volba!")
    nezadano = True
    while nezadano:
        odpoved = input("Přejete si zadat další volbu? [ano/ne]")
        if (odpoved == "ano" or odpoved == "ANO"):
            nezadano = False
        elif (odpoved == "ne" or odpoved == "NE"):
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nProgram ukončíte stiskem klávesy Enter...")





