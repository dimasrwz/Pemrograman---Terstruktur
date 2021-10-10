# menghitung jumlah mahasiswa

jmlLaki = int(input("jumlah mahasiswa laki-laki : "))
jmlPerempuan = int(input("jumlah mahasiswa perempuan : "))

hitung = jmlLaki // 10
print("\nLaki-laki : ", "*" * hitung,jmlLaki)

hitung = jmlPerempuan // 10
print("Perempuan : ", "*" * hitung,jmlPerempuan)
