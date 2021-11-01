# Latihan 4

def sum(*n):
    i = 0
    for x in n:
        i += i + x

    return i

def average(*n):
    i = 0
    j = 0
    for x in n:
        i = i + x
        j += 1
    average = i / j
    return average

def maks(*n):
    maks = n[0]
    for i in n:
        if maks < i:
            maks = i

    return maks

def min(*n):
    min = n[0]
    for i in n:
        if min > i:
            min = i

    return min
