try:
    file = input('Nama file yang ingin dienkripsi : ')
    key = int(input('Input key                       : '))
    dataFile = open(file + '.encrypt', 'r')
    isi = dataFile.read()
    hasil = ' '

    for i in isi:
        if i ==' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) - key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) - key - 65) % 26 + 65)
        
    dataFile.close()
    enkripsi = open(file + '.encrypt.decrypt', 'w')
    enkripsi.write(hasil)
    enkripsi.close()
    print('File enkripsi : {}.encrypt.decrypt'.format(file))

except FileNotFoundError:
    print('File tidak ditemukan')
