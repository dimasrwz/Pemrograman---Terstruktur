from datetime import *

def diffDate(x):
        skrg = datetime.date(datetime.now())
        tanggal = datetime.strptime(x, '%Y-%m-%d').date()
        selisih = skrg - tanggal
        selisih = selisih.days
        return selisih

def cariKode(kode):
    try:
        dataFile = open('DataPeminjamanBuku.txt', 'r')
        isi = dataFile.read()
        data = isi.replace('\n', '|')
        data = data.split('|')
        extract = data.index(kode)
        if kode in data:
            print('='*50)
            print('Data Peminjaman Buku'.rjust(34))
            print('='*50)
            print('Kode Member\t\t\t:', data[extract])

            print('Nama Member\t\t\t:', data[extract + 1])
            print('Judul Buku\t\t\t:', data[extract + 2])
            print('Tanggal Mulai Peminjaman\t:', data[extract + 3])
            print('Tanggal Maks Peminjaman\t\t:', data[extract + 4])
            print('Masukkan Tanggal Pengembalian\t:', datetime.date(datetime.now()))
            terlambat = diffDate(data[extract + 4])
            if terlambat > 0:
                print('Terlambat Pengembalian\t\t:', terlambat, 'hari')
                denda = int(terlambat) * 2000
                print('Denda\t\t\t\t: Rp.', denda)
            else:
                print('Tepat Waktu')

    except ValueError:
        print('Data Tidak Ditemukan')

ulang = 'y'
while ulang == 'y':
    kode = input('Masukkan Kode Number\t\t: ')
    data = cariKode(kode)
    ulang = input('Ulangi ? (y/n)\t\t\t: ')
    ulang = ulang.lower()
        
