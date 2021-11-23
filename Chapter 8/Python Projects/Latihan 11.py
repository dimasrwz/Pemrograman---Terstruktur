buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('===========================================================')
print('Daftar harga buah per/Kg : ')
print(buah)
print('===========================================================')
brp = []
total = []
while True:
    print('Menu : ')
    print('A. Tambah data buah')
    print('B. Beli buah')
    menu = input('Pilihan Menu : ')

    if menu == 'A' or menu == 'a':
        tambah = input('Masukkan nama buah    : ')
        if tambah in buah:
            print('Nama buah sudah ada')
        else:
            harga = int(input('Masukkan harga satuan : '))
            buah[tambah] = harga
            print('Data buah : ')
            for x, y in buah.items():
                print('')
                print('-', x, '( Harga Rp' + str(y) + ')')

    elif menu == 'B' or menu == 'b':
        while True:
            beli = input('Buah yang akan dibeli        : ')
            if beli in buah:
                kg = int(input('Berapa Kg yang akan dibeli   : '))
                lagi = input('Beli buah yang lain? (y/n)   : ')
                if lagi == 'y':
                    total = buah[beli] * kg
                    brp.append(total)
                elif lagi == 'n':
                    total = buah[beli] * kg
                    brp.append(total)
                    print('-----------------------------------------------------')
                    print('Total Harga                        : ', sum(brp))
                    break
                else:
                    print('Input tidak valid')
            else:
                print('Buah tidak tersedia')
    else:
        print('Input tidak valid')
    break
                         
            
