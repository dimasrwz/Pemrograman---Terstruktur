print('----------------------------------------')
print('        PROGRAM HITUNG RATA-RATA       ')
print('----------------------------------------')

n = 0
sum = 0
while True:
    try:
        bil = int(input('Masukkan bilangan bulat : '))
        n += 1
        sum = sum + bil
        lagi = input('lagi (y/n)? : ')
        if lagi == 'n':
            rata = sum / n
            print ('')
            print('Rata-ratanya adalah : ', rata)
            break
        elif lagi != 'y':
            break
    except ValueError:
        print('Bukan bilangan bulat')
