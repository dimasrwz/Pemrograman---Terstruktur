print ('Status Kelulusan Ujian Mahasiswa\n')

bIndo = int(input('Masukkan nilai Bhs Indonesia : '))
IPA = int(input('Masukkan nilai IPA           : '))
mtk = int(input('Masukkan nilai Matematika    : '))

print('========================================')

if (bIndo < 60) or (IPA < 60):
    print('status kelulusan             : TIDAK LULUS')
elif (mtk < 70):
    print('status kelulusan             : TIDAK LULUS')
else:
    print('status kelulusan             : LULUS')


