dataFile = open('datamahasiswa.txt', 'r')
data = dataFile.read()
data = data.replace('|', ' ')
data = data.replace('\n', ' ')
data = data.split(' ')

while True:
    cari = input('Masukkan NIM yang mau dicari : ')
    if cari in data:
        search = data.index(cari)
        print('Data Mahasiswa')
        print('NIM            : ', data[search])
        print('Nama Mahasiswa : ', data[search + 1])
        print('Alamat         : ', data[search + 2])
    else:
        print('Data tidak ditemukan')

    lagi = input('Ulangi lagi (y/n) ? ')
    lagi = lagi.lower()
    if lagi in ('N', 'n'):
        break

