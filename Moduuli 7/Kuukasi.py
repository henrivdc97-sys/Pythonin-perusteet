# Vuodenajat kuukausittain tammikuusta joulukuuhun
vuodenajat = (
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi"
)
#Pyydetään käyttäjältä luku 1-12
kuukausi = int(input("Anna kuukauden numero (1-12): "))
#Kerrottaan käyttäjälle vuoden aika. Muu kuin 1-12 on virheellinen syöttö
if 1 <= kuukausi <= 12:
    print("Vuodenaika on", vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukauden numero.")