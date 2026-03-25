# Funktio hakee listan. Parillisten lukujen jakojäännös on o, kun ne jakaa kahdella
def karsi_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

# Kutsutaan funktio laskemaan listan luvut ja tulostetaan parilliset luvut ja alkuperäinen lista
luvut = [1, 2, 4, 7, 11, 14, 6, 8]
karsittu = karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Parilliset luvut:", karsittu)