def suurin_arvo(a, b, c):
    return max(a, b, c)

luku1 = float(input("Anna luku 1:"))
luku2 = float(input("Anna luku 2:"))
luku3 = float(input("Anna luku 3:"))

arvo = suurin_arvo(luku1, luku2, luku3)


print(f"suurin arvo {arvo}")