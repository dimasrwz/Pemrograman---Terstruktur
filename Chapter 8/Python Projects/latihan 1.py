listAngka = []
bil = int(input('Tulislah banyaknya bilangan yang akan dimasukkan : '))
print('')

for i in range(bil):
    angka = int(input('Masukkan angka : '))
    listAngka.append(angka)
    
listAngka.sort(reverse = True)
print('')
dprint('Urutan besar ke kecil dari angka yang sudah dimasukkan adalah', listAngka)
