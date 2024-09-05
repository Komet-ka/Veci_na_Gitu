class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - get variable value
    def age(self):
        return self.__age

    @age.setter  # setter - set variable new value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter  # deleter - remove variable
    def age(self):
        self.__age = None


my_dog = Animal("pejsek fido", 34)
my_dog.age = -5  # Set age - using setter

print(my_dog.age)  # read age - using getter
del my_dog.age  # Remove variable - using deleter
print(my_dog.age)