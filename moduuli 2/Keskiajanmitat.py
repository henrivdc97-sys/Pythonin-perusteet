#tehtävä 5
leiviskat = float(input("Anna leiviskät"))
naulat = float(input("Anna naulat"))
luodit = float(input("Anna luodit"))


grammat = (
    leiviskat * 20 * 32 * 13.3 +
    naulat * 32 * 13.3 +
    luodit * 13.3
)

kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {jaannos_grammat} grammaa.")