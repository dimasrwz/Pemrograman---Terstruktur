# Waktu rental
# Rental dimulai pukul 06.00-23.50
jamAwal = 6
menitAwal = 0
jamAkhir = 23
menitAkhir = 50

# Biaya rental 12 jam pertama
tarif1 = 200000
 
# Biaya rental per jam
tarif2 = 10000

# Selisih waktu rental
slshJam = jamAkhir - jamAwal
slshMenit = menitAkhir - menitAwal

# Total biaya rental
totalBiaya = tarif1 + tarif2 *(slshJam -12)
totalBiaya = totalBiaya + tarif2 * (slshMenit / 60)
totalBiaya = round(totalBiaya)

print('Total durasi rental adalah', slshJam, 'Jam', slshMenit, 'Menit' )
print ('Total biaya rental adalah Rp', totalBiaya)

