#tehtävä 2

#kysytään hyttiluokka
hyttiluokka = input('Anna hyttluokka (LUX, A , B, C):')
#hyttiluokan kuvaus
if(hyttiluokka=='LUX'):
    print('LUX on parvekkeellinen hytti yläkannella.')
elif(hyttiluokka=='A'):
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif(hyttiluokka=='B'):
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif(hyttiluokka=='C'):
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('virheellinen hyttiluokka')


