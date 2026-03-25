# Funktio muutta litrat gallonoiksi
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


# Ohjelma palauttaa gallonat litroina kunnes tulee negatiivinen luku
while True:
    maara = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))

    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print(f"{litrat:.2f} litraa")