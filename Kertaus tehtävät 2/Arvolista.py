lista = []

while True:
    luku = int(input("Anna kokonaisluku 0 lopettaa ohjelman"))

    if luku == 0:
        break

    lista.append(luku)

    print(f"Uusinluku {luku}")
    print(f"lista nyt {lista}")
    print("järjestyksenä", sorted(lista))












