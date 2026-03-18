#luodaan lista luvuille
luvut = []

for i in range(1000):  #luvut voidaan pyttää 1000 kertaa
    syote = input("Anna luku (tyhjä lopettaa): ") #pyydetään luku

    if syote == "": #tyhjä syöte lopettaa ohjelman
        break

    luvut.append(float(syote) #lisätään luvut listaan

luvut.sort(reverse=True) # luvut suurimmasta pieninmpään

print("Viisi suurinta lukua:") #tulostetaan suurimmat luvut
for luku in luvut[:5]:
    print(luku)

