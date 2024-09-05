from DedicnostVicenasobna import Osoba


class Student(Osoba):
    def __init__(self, name, age, scholarship):
        Osoba.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    @classmethod
    def create_from_string(cls, inscription):
        name, age, scholarship = inscription.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 3:
            return True
        return False



stud1 = Student("Margaret", 32, 0)
stud2 = Student.create_from_string("Mark 21 600")
print(stud1.show_finance())
print(stud2)
print(Student.is_name_correct("alice"))
# ukazka spatneho kodu, ktery ale projde
#print(stud1.is_name_correct("Pavel"))
#stud3 = stud1.create_from_string("Pavel 41 600")
#print(stud3)