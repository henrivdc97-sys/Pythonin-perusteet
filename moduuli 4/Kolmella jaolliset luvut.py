
#Aloitetaan luvusta 1
luku = 1

#Generoidaan lukuja tuhanteen asti. Jakojäännöksen ollessa 0 luku on kolmella jaollinen.
#Lisätään lukuun aina 1 tuhanteen asti
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1
