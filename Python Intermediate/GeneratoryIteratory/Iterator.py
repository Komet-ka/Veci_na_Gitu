from math import sqrt
def je_prvocislo(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
class PrvociselnyIterator:
    # Iterator that iterates over n primes
    def __init__(self, n):
        self.n = n
        self.vygenerovana_cisla = 0
        self.cislo = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.cislo += 1
        if self.vygenerovana_cisla >= self.n:
            raise StopIteration
        elif je_prvocislo(self.cislo):
            self.vygenerovana_cisla += 1
            return self.cislo
        return self.__next__()


iter = PrvociselnyIterator(3)
for elem in iter:
    print(elem)

for elem in PrvociselnyIterator(3):
    print(elem)