print ('Status Kelulusan Ujian Mahasiswa\n')

bIndo = int(input('Masukkan nilai Bhs Indonesia : '))
IPA = int(input('Masukkan nilai IPA           : '))
mtk = int(input('Masukkan nilai Matematika    : '))

print('===========================================')

if (bIndo < 0) or (bIndo > 100):
    print('Maaf input ada yang tidak valid')
elif (mtk < 0) or (mtk > 100):
    print('Maaf input ada yang tidak valid')
elif (IPA < 0) or (IPA > 100):
    print('Maaf input ada yang tidak valid')


    if (bIndo < 60) or (IPA < 60):
        print('status kelulusan : TIDAK LULUS')
    elif (mtk < 70):
        print('status kelulusan : TIDAK LULUS')
    else:
        print('status kelulusan : LULUS')

