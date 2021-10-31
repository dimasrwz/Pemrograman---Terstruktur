def faktorial(n):
    fak = 1
    for i in range(1, n+1):
        fak *= i

    return fak

def kombinasi(p, q):
    kombinasi = faktorial(p)/(faktorial(q)*faktorial(p-q))
    print(kombinasi)

def permutasi(p, q):
    permutasi = faktorial(p)/faktorial(p-q)
    print(permutasi)

kombinasi(5, 3)
permutasi(10, 7)
