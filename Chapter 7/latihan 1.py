try:
    nama = input('Masukkan Nama File : ')
    print('Isi File', nama, 'adalah  : ')
    print ('')
    file = open(nama, 'r')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
