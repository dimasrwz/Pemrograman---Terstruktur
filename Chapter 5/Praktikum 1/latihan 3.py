print ('Status Kelulusan Ujian Mahasiswa\n')

bIndo = int(input('Masukkan nilai Bhs Indonesia : '))
IPA = int(input('Masukkan nilai IPA           : '))
mtk = int(input('Masukkan nilai Matematika    : '))

print('===========================================')

if (bIndo < 60) or (IPA < 60):
        print('status kelulusan             : TIDAK LULUS')
        print('sebab                        :')
elif (mtk < 70):
        print('status kelulusan             : TIDAK LULUS')
        print('sebab                        :')
else:
        print('status kelulusan : LULUS')
       

if (bIndo < 60):
    print('- Nilai Bahasa Indonesia kurang dari 60')
if (mtk < 70):
    print('- Nilai matematikanya kurang dari 70')
