from math import sqrt
def je_prvocislo(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def prvociselny_generator(n):
    cislo = 2
    vygenerovana_cisla = 0
    while vygenerovana_cisla != n:
        if je_prvocislo(cislo):
            yield cislo
            vygenerovana_cisla += 1
        cislo += 1


gen = prvociselny_generator(3)
for elem in gen:
    print(elem)