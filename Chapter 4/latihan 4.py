# Jarak
jarakAkeB = 125
jarakBkeC = 256

# Kecepatan atau V
V1 = 62
V2 = 70

# Berangkat
waktuBerangkat = 06.00

# Istirahat
waktuIstirahat = 45 / 60

# Hitung waktu
waktu1 = jarakAkeB // V1
waktu2 = jarakBkeC // V2
totalWaktu = (waktu1 + waktu2)
  
# Total
sampai = waktuBerangkat + totalWaktu + waktuIstirahat


print('Jadi, Pak Amir sampai di Kota C pukul', sampai)
