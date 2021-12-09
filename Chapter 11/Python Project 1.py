from datetime import *

def diffDate(x):
        skrg = datetime.date(datetime.now())
        tanggal = datetime.strptime(x, '%Y-%m-%d').date()
        selisih = skrg - tanggal
        selisih = selisih.days
        print('Tanggal sekarang\t\t: ', skrg)
        print('Selisih\t\t\t\t: ', selisih, 'hari')
        return selisih

tgl = input('Masukkan tanggal (YYYY-MM-DD)\t:  ')
diffDate(tgl)
