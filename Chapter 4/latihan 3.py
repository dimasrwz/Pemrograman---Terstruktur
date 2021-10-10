jarakKota = 795
jarakPerLiter = 12
maksTangki = 50

# Penggunaan bensin
totalBensin = jarakKota / jarakPerLiter

# Banyak isi bensin
isiBensin = int(totalBensin // maksTangki)

# Menampilkan Hasil
print('Total Bensin yang diperlukan untuk sampai di kota C adalah', totalBensin, 'Liter')
print('Minimal mengisi bensin', isiBensin, 'kali')

