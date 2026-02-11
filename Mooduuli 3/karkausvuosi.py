#teht 4

#kysytään vuosi
vuosi = int(input('Anna vuosiluku:'))

#annettaan kaava, jolla saadaan karkausvuodet
if (vuosi % 4 == 0 and vuosi % 100 != 0) or vuosi % 400 == 0:
    print("vuosi on karkausvuosi")

else:
    print("Vuosi ei ole karkausvuosi")

