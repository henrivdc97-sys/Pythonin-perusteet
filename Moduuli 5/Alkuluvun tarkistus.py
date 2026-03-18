#pyydetään kokonaisluku
n = int(input("Anna kokonaisluku: "))

#luku ei voi olla alkuluku, jos se on < 2
if n < 2:
    print("Ei ole alkuluku.")
else:
    on_alkuluku = True #"oletetaan" olevan alukuluku
#Silmukka tarkistaa kaikkien lukujen jakojäännöksen ennen annettua lukua. jos jakojäännös on 0 luku ei ole alkuluku
    for i in range(2, n):
        if n % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")