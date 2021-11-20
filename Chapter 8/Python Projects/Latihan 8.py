def ratarata(a):
    rata = sum(buah.values()) / len(buah)
    return rata

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
print('Rata - rata harga satuan nya adalah', ratarata(buah))
