
nimi = input('Anna nimesi:')
print(f'Terve, {nimi}!')

import math

sade = float(input("Anna ympyrän säde: "))
pinta_ala = math.pi * sade ** 2
print(pinta_ala)

kanta = float(input('Anna suorakulmion kanta'))
korkeus = float(input('Anna suorakulmion korkeus'))

pinta_ala = kanta * korkeus
Piiri = 2 * kanta + 2 * korkeus

print(pinta_ala)
print(Piiri)

luku1, luku2, luku3 = map(int, input('Anna kolme lukua').split())

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(summa)
print(tulo)
print(keskiarvo)

leiviskat = float(input("Anna leiviskät"))
naulat = float(input("Anna naulat"))
luodit = float(input("Anna luodit"))

# Muunnokset grammoiksi
grammat = (
    leiviskat * 20 * 32 * 13.3 +
    naulat * 32 * 13.3 +
    luodit * 13.3
)

kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {jaannos_grammat} grammaa.")



