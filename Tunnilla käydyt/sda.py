def inventaario(tavarat):
    print("sinulla on seuraavat tavarat repussa: ")
    for t in tavarat:
        print("-" + t)
    tavarat.clear()
    return

#pääohjelma
reppu = ["taskulamppu", "Otsalamppu", "pöytälamppu"]

inventaario(reppu)

reppu.append("Eväsleipä")
inventaario(reppu)
