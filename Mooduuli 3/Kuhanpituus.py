
#tehtävä 1
#Kysytään kuhan pituutta
pituus = float(input('Anna kuhan pituus senttimetreinä'))

alamitta = 37
#katsotaan saako kuhan pyydystää
if pituus <= alamitta:
    puuttuu = alamitta - pituus
    print('kuha on alamittainen')
    print(f'laske kuha takaisin järveen. Pituudesta puuttuu{puuttuu} cm')
else:
    print('kuhan voi pyydystaa')










