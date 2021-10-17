hitung = 0
sum = 0
for i in range(100):
    if (i % 2 == 1):
        print(i)
        hitung = hitung + 1
        sum = sum + i

print('Banyaknya bilangan ganjil : ', hitung)
print('Jumlah seluruh bilangan   : ', sum)
