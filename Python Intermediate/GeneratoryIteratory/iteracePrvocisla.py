from math import sqrt


def je_prvocislo(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def vrat_n_prvocisel(n):
    prvocisla = []
    i = 2
    while len(prvocisla) != n:
        if je_prvocislo(i):
            prvocisla.append(i)
        i += 1
    return prvocisla


lst = vrat_n_prvocisel(1000000)
for elem in lst:
    print(elem)