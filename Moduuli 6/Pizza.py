# Otetaan matemaattiset toiminnot käyttöön
import math
# Funktio hakee pizzan halkasijan ja hinnan. Lasketaan funktion avulla pizzan pinta-ala ja jaetaan se pizzan hinnalla
def pizzan_yksikkohinta(halkaisija_cm, hinta_euroina):
    sade_m = (halkaisija_cm / 2) / 100  # cm → m
    pinta_ala = math.pi * sade_m ** 2
    return hinta_euroina / pinta_ala

# h=hinta ja p= pizza. Pyydetään molempien pizzojen hinnat ja halkaisijat.
h1 = float(input("Anna pizzan 1 halkaisija (cm): "))
p1 = float(input("Anna pizzan 1 hinta (€): "))

h2 = float(input("Anna pizzan 2 halkaisija (cm): "))
p2 = float(input("Anna pizzan 2 hinta (€): "))

# kutustaan funktiota molemmille pizzoille.
y1 = pizzan_yksikkohinta(h1, p1)
y2 = pizzan_yksikkohinta(h2, p2)

# Tulostetaan pizzojen hinnat per M2
print(f"Pizza 1 yksikköhinta: {y1:.2f} €/m²")
print(f"Pizza 2 yksikköhinta: {y2:.2f} €/m²")


if y1 < y2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif y2 < y1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")