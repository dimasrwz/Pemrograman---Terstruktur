dataFile = open('databil.txt', 'r')
for i in dataFile:
    ambil = i.split('|')
    hasil = int(ambil[0]) + int(ambil[1])
    print(hasil)

dataFile.close()
