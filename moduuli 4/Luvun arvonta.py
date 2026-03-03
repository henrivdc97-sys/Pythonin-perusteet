#tuodaan random luvut
import random

#Arvotaan luku 1-10
salainen_luku = random.randint(1, 10)

#Käytetään while rakennetta
while True:
    arvaus = int(input("Arvaa luku (1-10): "))

#if rakenteella selvitetääb luku
    if arvaus > salainen_luku:
        print("Liian suuri arvaus")
    elif arvaus < salainen_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break