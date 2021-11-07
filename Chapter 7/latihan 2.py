namaFile = input('Masukkan Nama File : ')
try:
    file = open(namaFile, 'r')
    lagi = 'y'
    while (lagi == 'y'):
        file = open(namaFile, 'a')
        xxx = input('Data yang mau ditambahkan : ')
        file.write(xxx)
        lagi = input('Mau lagi (y/n) : ')
        file.close()
except FileNotFoundError:
    print('File tidak ada / salah penulisan')
