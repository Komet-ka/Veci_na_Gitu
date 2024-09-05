for i in range(1,11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1

from math import sqrt
def je_prvocislo(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

pocet_prvocisel = 0
cislo = 2
prvocisla = []

while pocet_prvocisel < 100 and cislo < 1000:
    if je_prvocislo(cislo):
        prvocisla.append(cislo)
        pocet_prvocisel +=1
    cislo += 1

print(len(prvocisla))
print(prvocisla[-1])
print(cislo)