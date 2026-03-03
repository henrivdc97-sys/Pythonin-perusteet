
#Asetetaan yrityksen nollaan
yritykset = 0

#Asetetaan käyttäjälle 5 yritystä
while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
#asetetaan käyttäjätunnus ja salasana.
#Väärin mennyt lisää yhden yrityksen ja pyytää tunnuksia uudelleen
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana.")
        yritykset += 1
# viiden väärän yrityksen jälkeen ohjelma evää pääsyn
if yritykset == 5:
    print("Pääsy evätty")