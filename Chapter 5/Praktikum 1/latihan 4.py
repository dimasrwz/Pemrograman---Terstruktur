kode = input('Masukkan kode karyawan   : ')
nama = input('Masukkan nama karyawan   : ')
gol  = input('Masukkan golongan        : ')


if(gol == 'A' ):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 2.5 / 100 * 10000000
elif(gol == 'B'):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 2.0 / 100 * 8500000
elif(gol == 'C'):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 1.5 / 100 * 7000000
elif(gol == 'D'):
    gajiPokok = 5500000
    potongan = 1.0
    jumlahPotongan = 1.0 / 100 * 5500000

gajiBersih = gajiPokok - jumlahPotongan

print('\n=======================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('---------------------------------------')
print('Nama karyawan            :', nama + '(kode :', kode + ')')
print('Golongan                 :', gol)
print('---------------------------------------')
print('Gaji Pokok               : Rp', gajiPokok)
print('Potongan (' + str(potongan) + '%)          : Rp', int(jumlahPotongan))
print('--------------------------------------- -')
print('Gaji Bersih              : Rp', int(gajiBersih))
      
      
