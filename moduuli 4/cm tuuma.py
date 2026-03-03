
# pyydetään tuumia kunnes annettaan negatiivin luku
while True:
    tuumat = float(input("anna tuuma maara (negatiivinen luku lopettaa):"))

#neg luku lopettaa ohjelman
    if tuumat < 0:
        print("ohjelma lopetetaan")
        break
#Muunnettaan tuumat senttimetreiksi
    senttimetrit = tuumat * 2.54
    print(f"{senttimetrit} cm")

