def nilai(nilaiMhs):
    nama = {}
    nim = {}
    for i in range (len(nilaiMhs)):
        nilaiAkhir = ((nilaiMhs[i]['mid']) + (2 * (nilaiMhs[i]['uas'])))/3
        nama[nilaiMhs[i]['nama']] = nilaiAkhir
        nim[nilaiMhs[i]['nim']] = nilaiAkhir
    namaMhs = max(nama, key = nama.get)
    nimMhs = max(nim, key = nim.get)
    print('Mahasiswa yang memiliki nilai akhir tertinggi adalah ', namaMhs, 'dengan nim :', nimMhs)

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

nilai(nilaiMhs)
