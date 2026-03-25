import random

# Funktio saa parametrina nopan tahkojen määrän ja palauttaa saadun silmäluvun
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


# Käyttäjä antaa tahkojen määrän
tahkot = int(input("Anna nopan tahkojen määrä: "))

# Ohjelma tulostaa lukuja kunnes antaa nopan suurimman silmäluvun
while True:
    tulos = heita_noppaa(tahkot)
    print(tulos)

    if tulos == tahkot:
        break