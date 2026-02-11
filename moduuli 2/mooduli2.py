

#tehtävä 1
nimi = input('Anna nimesi:')
print(f'Terve, {nimi}!')

#tehtävä 2
import math

sade = float(input("Anna ympyrän säde: "))
pinta_ala = math.pi * sade ** 2
print(pinta_ala)

#tehtävä 3
kanta = float(input('Anna suorakulmion kanta'))
korkeus = float(input('Anna suorakulmion korkeus'))

pinta_ala = kanta * korkeus
Piiri = 2 * kanta + 2 * korkeus

print(pinta_ala)
print(Piiri)


#tehtävä 4
luku1, luku2, luku3 = map(int, input('Anna kolme lukua').split())

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(summa)
print(tulo)
print(keskiarvo)

#tehtävä 5
leiviskat = float(input("Anna leiviskät"))
naulat = float(input("Anna naulat"))
luodit = float(input("Anna luodit"))


grammat = (
    leiviskat * 20 * 32 * 13.3 +
    naulat * 32 * 13.3 +
    luodit * 13.3
)

kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {jaannos_grammat} grammaa.")

#tehtävä 6
import random


koodi3 = ""
for i in range(3):
    koodi3 += str(random.randint(0, 9))


koodi4 = ""
for i in range(4):
    koodi4 += str(random.randint(1, 6))

print("Kolmenumeroinen koodi (0–9):", koodi3)
print("Nelinumeroinen koodi (1–6):", koodi4)

