nilai = [{'nim' : 'A01', 'nama' : 'AGUSTINA', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'BUDI', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'CHICHA', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'DONNA', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'FATIMAH', 'mid' : 70, 'uas' : 100}]

print('=' * 70)
print('NIM'.ljust(8), 'NAMA'.ljust(16), 'N.MID'.ljust(10), 'N.UAS'.ljust(10),
      'N.AKHIR'.ljust(10), 'STATUS'.ljust(12))
print('-' * 70)


for i in nilai:
    nilaiAkhir = round((i.get('mid')+i.get('uas')*2)/3, 2)
    if nilaiAkhir >= 60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'

    print(i.get('nim').ljust(8),
         i.get('nama').ljust(16),
         str(i.get('mid')).ljust(10),
         str(i.get('uas')).ljust(10),
         str(nilaiAkhir).ljust(10),
         status.ljust(12))

print('=' * 70)
    
