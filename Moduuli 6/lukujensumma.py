# Funktio hakee annetun listan ja summaa luvut yhteen
def laske_summa(lista):
    return sum(lista)

# Listataan kokonaisluvut, kutsutaan funktio ja tulostetaan palautettu summa
luvut = [2, 2, 7, 4, 6]
tulos = laske_summa(luvut)
print("Listan summa:", tulos)