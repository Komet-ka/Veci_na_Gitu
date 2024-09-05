class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno} ma {self.vek} roku"


class Zamestnanec(Osoba):
    def __init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin):
        super().__init__(jmeno, vek)
        self.sazba = sazba
        self.pocet_odpracovanych_hodin = pocet_odpracovanych_hodin

    def vrat_vydelek(self):
        return self.sazba * self.pocet_odpracovanych_hodin


class Student(Osoba):
    def __init__(self, jmeno, vek, stipendium):
        super().__init__(jmeno, vek)
        self.stipendium = stipendium

    def vrat_vydelek(self):
        return self.stipendium


os1 = Osoba("Henry", 54)
os2 = Zamestnanec("Jack", 36, 20, 160)
os3 = Student("Agatha", 22, 1000)
print(os1)
print(os2)
print(os3)