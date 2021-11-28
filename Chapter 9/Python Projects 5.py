nilai = [{'nim' : 'A01', 'nama' : 'AGUSTINA', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'BUDI', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'CHICHA', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'DONNA', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'FATIMAH', 'mid' : 70, 'uas' : 100}]

print('=' * 50)
print('NIM'.ljust(10), 'NAMA'.ljust(10), 'N.MID'.rjust(10), 'N.UAS'.rjust(10))
print('-' * 50)

for i in nilai:
    print(i.get('nim').ljust(10),
          i.get('nama').ljust(15),
         str(i.get('mid')).ljust(10),
         str(i.get('uas')).ljust(10))

print('=' * 50)
