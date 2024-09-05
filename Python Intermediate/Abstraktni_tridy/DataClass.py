from AbstraktniTrida import Tvar
from dataclasses import dataclass

@dataclass
class Obdelnik(Tvar):
    a: int
    b: int

    def obvod(self):
        return 2 * (self.a + self.b)

    def obsah(self):
        return self.a * self.b

p1 = Obdelnik(3, 4)
p2 = Obdelnik(3, 4)
print(p1)
print(p1 == p2)