#Program input data mahasiswa

dataFile = open('datamahasiswa.txt', 'a')

while True :
    nim = input('Masukkan NIM            : ')
    nama = input('Masukkan nama mahasiswa : ')
    alamat = input('Masukkan alamat         : ')

    myString = nim + '|' + nama + '|' + alamat + '\n'
    dataFile.write(myString)

    lagi = input('Mau input data lagi (y/n) ? ')
    if lagi in ('N', 'n'):
        break

dataFile.close()
