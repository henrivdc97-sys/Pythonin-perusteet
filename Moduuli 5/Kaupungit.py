#luodaan lista
kaupungit = []
#pyydetään käyttäjältä kaupunki 5 kertaa ja lisätään listaan
for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

print("\nKaupungit järjestyksessä:") #luodaan tyhjärivi ennen tekstiä
#Tulostetaan kaupungit yksi kerralaan järjestyksessä
for kaupunki in kaupungit:
    print(kaupunki)