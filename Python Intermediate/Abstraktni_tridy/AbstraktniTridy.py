from abc import ABC, abstractmethod
from math import pi


class Tvar(ABC):
    @abstractmethod
    def obvod(self):
        pass

    @abstractmethod
    def obsah(self):
        pass

#o = Tvar()

class Obdelnik(Tvar):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obvod(self):
        return 2 * (self.a + self.b)

    def obsah(self):
        return self.a * self.b


class Kruh(Tvar):
    def __init__(self, r):
        self.r = r

    def obvod(self):
        return 2 * self.r * pi

    def obsah(self):
        return pi * self.r ** 2

if __name__ == '__main__':
    ob1 = Obdelnik(3, 5)
    ob2 = Obdelnik(3, 5)
    kruh1 = Kruh(12)
    print(ob1.obvod())
    print(kruh1.obvod())
    print(ob1 == ob2)