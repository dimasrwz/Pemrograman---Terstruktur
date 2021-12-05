# Program baca data Mahasiswa

dataFile = open('datamahasiswa.txt', 'r')

dataList = []

data = dataFile.readlines()

for i in range(len(data)):
    pecahData = data[i].split('|')
    dataDict = {'NIM' : pecahData[0],
                'nama mahasiswa' : pecahData[1],
                'alamat' : pecahData[2].replace('\n', ' ')}
    dataList.append(dataDict)
    

print(dataList)

dataFile.close()

