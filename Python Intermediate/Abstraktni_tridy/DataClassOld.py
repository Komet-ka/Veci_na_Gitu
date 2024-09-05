from AbstraktniTrida import Tvar
class Obdelnik(Tvar):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"Obdelnik(a={self.a}, b={self.b})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Obdelnik) and (self.a, self.b) == (other.a, other.b)

    def obvod(self) -> float:
        return 2 * (self.a + self.b)

    def obsah(self) -> float:
        return self.a * self.b

p1 = Obdelnik(3, 4)
p2 = Obdelnik(3, 4)
print(p1)
print(p1 == p2)