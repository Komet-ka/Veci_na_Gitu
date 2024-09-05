def je_sude_cislo(cislo):
    if cislo % 2 == 0:
        return True

def generatorSudychCisel(n):
    cislo = 1
    vygenerovana_cisla = 0
    while vygenerovana_cisla != n:
        if je_sude_cislo(cislo):
            yield cislo
            vygenerovana_cisla += 1
        cislo += 1


gen = generatorSudychCisel(3)
for elem in gen:
    print(elem)