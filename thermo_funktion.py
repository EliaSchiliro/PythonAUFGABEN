

def malethermometer(temp, max):
    print('    _ ')
    r = range(max, 0, -1)
    for x in r:
        thermo_zeile(x, temp)
    print('   (_)')

def thermo_zeile(zeile, temp):
    filler = '|-|'
    prefix = '   ' 
    if zeile == temp or zeile < temp:
        filler = '|||' 
    if zeile % 5 == 0:
        if zeile < 10:
            prefix = str(zeile) + '  '
        else:
            prefix = str(zeile) + " "

    print(prefix + filler)

malethermometer(14,30)