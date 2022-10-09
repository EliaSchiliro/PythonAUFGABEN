temp = 20

print('    _ ')
for x in range(35, 0, -1):
    filler = '|-|'
    prefix = '   ' 
    if x == temp or x < temp:
        filler = '|||' 
    if x % 5 == 0:
        if x < 10:
            prefix = str(x) + '  '
        else:
            prefix = str(x) + " "

    print(prefix + filler)
    


print('   (_)')



