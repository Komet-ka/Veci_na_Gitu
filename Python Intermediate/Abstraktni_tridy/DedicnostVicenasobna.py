class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno} ma {self.vek} roku"


class Zamestnanec(Osoba):
    def __init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin):
        Osoba.__init__(self, jmeno, vek)
        self.sazba = sazba
        self.pocet_odpracovanych_hodin = pocet_odpracovanych_hodin

    def vrat_vydelek(self):
        return self.sazba * self.pocet_odpracovanych_hodin


class Student(Osoba):
    def __init__(self, jmeno, vek, stipendium):
        Osoba.__init__(self, jmeno, vek)
        self.stipendium = stipendium

    def vrat_vydelek(self):
        return self.stipendium

class PracujiciStudent(Zamestnanec, Student):
    def __init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin, stipendium):
        Zamestnanec.__init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin)
        Student.__init__(self, jmeno, vek, stipendium)

    def vrat_vydelek(self):
        return self.sazba * self.pocet_odpracovanych_hodin + self.stipendium

# PracujiciStudent => Zamestanec => Student => Osoba
if __name__ == "__main__":
    os1 = Osoba("Henry", 54)
    os2 = Zamestnanec("Jack", 36, 20, 160)
    os3 = Student("Agatha", 22, 1000)
    os4 = PracujiciStudent("Monica", 24, 9.5, 70, 550)
    print(os1)
    print(os2)
    print(os3)
    print(os4)