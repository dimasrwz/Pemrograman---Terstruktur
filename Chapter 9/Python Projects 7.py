mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('=' * 60)
print('NIM'.ljust(6),
      'NAMA MAHASISWA'.ljust(20),
      'TGL LAHIR'.ljust(15),
      'TEMPAT LAHIR'.ljust(15))
print('-' * 60)

for isi in mhs:
        isiList = isi.split(':')
        lahir = isiList[2].split('-')
        tglLahir = lahir[2] + '/' + lahir[1] + '/' + lahir[0]
        print(isiList[0].ljust(6, ' '), isiList[1].ljust(20,' '), tglLahir.ljust(15, ' '), isiList[3].ljust(15, ' '))

                
print('-' * 60)
