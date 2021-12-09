from datetime import *

dataFile = open('DataPeminjamanBuku.txt', 'a') 

while True:
        kode = input('Masukkan Kode Member\t: ')
        nama = input('Masukkan Nama Member\t: ')
        judul = input('Masukkan Judul Buku\t: ')
        tanggal = datetime.date(datetime.now())
        tanggalKembali = tanggal + timedelta(days=7)
        listData = [kode, nama, judul, str(tanggal), str(tanggalKembali)]
        dataFile.write('|'.join(listData) + '\n')

        lagi = input('Ulangi lagi? (y/n)\t: ')
        if lagi in ('n', 'N'):
                break

dataFile.close()
