from dataclasses import dataclass, InitVar, field

@dataclass
class Tester:
    prvni_int: InitVar[int]
    multiplikator: int
    seznam_celych_cisel: list[int]
    druhy_int: int
    vypoctena_hodnota: float = field(init=False)

    def __post_init__(self, prvni_int):
        self.vypoctena_hodnota = prvni_int * self.multiplikator * sum(self.seznam_celych_cisel) - self.druhy_int

    def __eq__(self, other):
        return self.vypoctena_hodnota == other.vypoctena_hodnota

    def __call__(self):
        return self.vypoctena_hodnota


o1 = Tester(0, 1, [2, 4.0], 4)
o2 = Tester(0, 8, [1, 45], 3)

#print(o1.prvni_int) #hodi error
#print(o1.vypoctena_hodnota) # nehodi error
print(o1)
print(o1==o2)
print(o1())