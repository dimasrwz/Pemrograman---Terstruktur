def kuadrat(bil):
    for i in range(len(bil)):
        bil[i]**=2
    return bil

bil = []
jumlah = int(input('Jumlah angka yang ingin diinputkan : '))
for i in range(jumlah):
    angka = int(input('Masukkan angka : '))
    bil.append(angka)

print('=====================================')
print(bil)
print(kuadrat(bil))

    
