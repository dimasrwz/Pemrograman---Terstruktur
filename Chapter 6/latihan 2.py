def starFormation1(n):
    baris = n
    i = 0
    while (i < baris):
            j = 0
            while (j <= i):
                print('* ', end='')
                j += 1
            print('')
            i += 1

def starFormation2(n):
    baris = 0
    i = n
    while(i >= baris):
            j = 1
            while(j < i):
                print('* ', end='')
                j += 1
            print('')
            i -= 1
            
starFormation1(4)
starFormation2(4)
