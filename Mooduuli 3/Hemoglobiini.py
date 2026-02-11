#tehtävä 3
#kysytään tiedot
sukupuoli = input('Anna biologinen sukupuoli nainen/mies:')
hb = float(input('Anna hemoglobiiniarvo (g/l):'))

#jaotellaan vastauksen perusteella kahtia ja katsotaan mihin hemoglobiini sijoittuu.
if sukupuoli == 'nainen':
    if hb < 117:
        print('Hemoglobiini on alhainen')
    elif 117 <= hb <= 175:
        print('hemogolibiini on normaali')
    else:
        print('hemoglobiini on korkea')

elif sukupuoli == 'mies':
    if hb < 134:
        print('hemoglobiini on alhainen')
    elif 134 <= hb <= 195:
        print('hemoglobiini on normaali')
    else:
        print('hemoglobiini on korkea')



