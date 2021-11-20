def maxValue(buah):
    nilaiMax = max(buah, key = buah.get)
    return nilaiMax

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
print('Harga paling mahal adalah buah',maxValue(buah))
