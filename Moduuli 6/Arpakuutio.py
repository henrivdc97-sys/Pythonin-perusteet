import random

# Parametriton funktio, joka palauttaa satunnaisen luvun 1–6
def heita_noppaa():
    return random.randint(1, 6)


# Noppaa heitetään niin kauan kunnes tulee 6
while True:
    tulos = heita_noppaa()
    print(tulos)

    if tulos == 6:
        break