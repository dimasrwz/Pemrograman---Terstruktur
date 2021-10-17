#Tebak angka

from random import randint
angka = randint(0, 100)

print('"Hai.. nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!"')
tebak = int(input('Tebakan Anda : '))
while True:
    if(tebak < angka):
        print('Hehehe...Bilangan tebakan anda terlalu kecil')
        tebak = int(input('Tebakan Anda : '))
    elif(tebak > angka):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
        tebak = int(input('Tebakan Anda : '))
    elif(tebak == angka):
        print('Yeeee3...Bilangan tebakan Anda BENAR :-) ')
        break

