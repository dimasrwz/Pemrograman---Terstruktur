def dataStat(x):
    average = sum(x) / len(x)
    maks = max(x)
    minimum = min(x)
    return[average, maks, minimum]

try:
    jumlah = int(input('Jumlah angka yang ingin di inputkan : '))
    print('')
    data = []
    for i in range(jumlah):
        angka = int(input('Masukan angka : '))
        data.append(angka)
except:
    print('Input tidak valid')

print('')
print('[Rata-rata, Max, Min] adalah', dataStat(data))
