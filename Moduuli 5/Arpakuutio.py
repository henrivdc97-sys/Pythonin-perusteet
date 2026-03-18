#Otetaan käyttöön random numerot
import random
#pyydetään arpakuutioiden määrä
maara = int(input("Kuinka monta arpakuutiota heitetään? "))
#Summataan nopat alussa 0
summa = 0
#toistetaan silmukka heittojen määrän verran. Satunnainen luku 1-6. Lisätää heitto summaan.
for i in range(maara):
    heitto = random.randint(1, 6)
    summa += heitto

print("Silmälukujen summa on:", summa)

