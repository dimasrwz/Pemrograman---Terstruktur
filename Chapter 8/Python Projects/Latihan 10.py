buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('===========================================================')
print('Daftar harga buah per/Kg : ')
print(buah)
print('===========================================================')
total = []
while True:
    beli = input('Buah yang dibeli : ')
    if beli in buah:
        kg = int(input('Berapa Kg        : '))
        harga = kg * buah[beli]
        total.append(harga)
        lagi = input('Beli buah yang lain (y/n)? ')
        if lagi != 'y':
            print('----------------------------')
            print('Total harga      : ', sum(total))
            break   
