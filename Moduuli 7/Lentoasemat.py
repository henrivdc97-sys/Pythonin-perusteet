lentoasemat = {} #Luodaan sanakirja

#kysytään käyttäjältä haluaako hän hakea, lisätä vai lopettaa.
while True:
    toiminto = input("Valitse toiminto (lisaa / hae / lopeta): ").lower()
#Lentoaseman ja ICA0 koodin lisäys
    if toiminto == "lisaa":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    # Lentoaseman ja ICA0 koodin haku
    elif toiminto == "hae":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")
#lopetus
    elif toiminto == "lopeta":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta.")