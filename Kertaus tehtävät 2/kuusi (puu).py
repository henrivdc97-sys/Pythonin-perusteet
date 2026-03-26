def kuusi(korkeus):
    print("Tämä on kuusi!")


    for k in range(1,korkeus + 1):

        valit_alku = korkeus - k

        tahdet = k * 2 - 1

        print(" " * valit_alku + "*" * tahdet)

    print(" " * (korkeus - 1) + "*")

kuusi(5)

kuusi(6)


