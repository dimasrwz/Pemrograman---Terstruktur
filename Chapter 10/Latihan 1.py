# membaca bilangan

dataFile = open('bilangan.txt', 'r')
genap = 0
ganjil = 0
for i in dataFile:
    if int(i) % 2 == 0:
        genap += 1
    else:
        ganjil += 1

dataFile.close()
hasil = {'genap' : genap, 'ganjil' : ganjil}
print('Banyaknya bilangan genap  : ', hasil.get('genap'))
print('Banyaknya bilangan ganjil : ', hasil.get('ganjil'))
