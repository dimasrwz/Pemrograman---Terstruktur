data = []

jumlah = int(input('Jumlah mahasiswa yang ingin di inputkan : '))

for i in range(jumlah):
    nama = input('Masukkan Nama Mahasiswa : ')
    data.append(nama)
    
print('===================================')  
for nama in data:
    print(nama, '(', len(nama), 'karakter', ')')
               
