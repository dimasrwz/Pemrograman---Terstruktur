sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print('Sayur :', sayur)
while True:
    print('Menu : ')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    pilihan = input('Masukkan pilihan Anda : ')
    if pilihan == 'A':
        tambah = input('Tulislah sayur yang ingin Anda tambahkan : ')
        sayur.append(tambah)
        print(tambah, 'telah dimasukkan ke dalam list')
        print('========================================')
    elif pilihan == 'B':
        try:
            hapus = input('Tulislah sayur yang ingin Anda hapus : ')
            sayur.remove(hapus)
            print(hapus, 'sudah dihapus dari list')
            print('====================================')
        except ValueError:
            print('Sayur tersebut tidak terdapat pada list')
    elif pilihan == 'C':
        print('========================================')
        print('Data Sayur : ', sayur)
        print('========================================')
        print('')
    else:
        break
        
