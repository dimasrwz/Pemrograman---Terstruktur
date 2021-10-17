kode = input('Masukkan kode karyawan   : ')
nama = input('Masukkan nama karyawan   : ')
gol  = input('Masukkan golongan        : ')
status = input('Masukkan status (1: menikah, 2: belum) : ')

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

if(status == '1'):
    tunjanganSuamiIstri = 10 / 100 * gajiPokok
    jumlahAnak = int(input('Masukkan Jumlah Anak : '))
    tunjanganAnak = 5 /100 *gajiPokok
    tunjanganAnak = jumlahAnak * tunjanganAnak
    statusMenikah = 'sudah menikah'
else:
    jumlahAnak = 0
    tunjanganSuamiIstri = 0
    tunjanganAnak = 0
    statusMenikah = 'belum menikah'

gajiKotor = gajiPokok + tunjanganSuamiIstri + tunjanganAnak
gajiBersih = gajiKotor - jumlahPotongan

print('\n=======================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('---------------------------------------\n')
print('Nama karyawan            :', nama + '(kode :', kode + ')')
print('Golongan                 :', gol)
print('Status Menikah           :', statusMenikah)
print('Jumlah Anak              :', jumlahAnak)
print('---------------------------------------')
print('Gaji Pokok               : Rp', gajiPokok)
print('Tunjangan Istri/Suami    : Rp', int(tunjanganSuamiIstri))
print('Tunjangan Anak           : Rp', int(tunjanganAnak))
print('--------------------------------------- +')
print('Gaji Kotor               : Rp', int(gajiKotor))
print('Potongan (' + str(potongan) + '%)          : Rp', int(jumlahPotongan))
print('--------------------------------------- -')
print('Gaji Bersih              : Rp', int(gajiBersih))
      
