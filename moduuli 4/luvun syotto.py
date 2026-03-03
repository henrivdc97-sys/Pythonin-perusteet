#Luodaan lista luvuille
luvut = []

#syöte pyytä lukuja niin kauan, kuin kenttä ei ole tyhjä
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    luku = float(syote)
    #lisätään luvut listaan
    luvut.append(luku)
#Katsotaan listan pituus, sekä isoin ja pienin lul
if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
