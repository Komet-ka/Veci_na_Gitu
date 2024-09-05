#1/0
#ZeroDivisionError
cislo = 3
pole = [1,0,2]

for i in pole:
    try:
        result = cislo/i
    except ZeroDivisionError:
        print("Tady delime nulou")
        continue
    print(f"Result is: {result}")

a = 2
b = 1

#assert a == b
#AssertionError

def moje_funkce (x,y):
    assert x is int
    assert len(y)>0

#x = 10
#AtribututeError
x = [10]
x.append(8)
print(x)

print(len("asdf"))
#len = 1
#len("asfd")
#TypeError

a = 1
b = 2

#test = a + b + "ahoj"
#TypeError

#f = open("text.txt")
#NameError

lst = [1,2,3,4]
#print(lst[6])
#IndexError

from os import getcwd
print(getcwd())
#from utils import calculate_diff
#ModuleNotFound

a = 10
a += 1
print(a)

#z += 1
#NameError

a = "Alice has a cat"
#b = int(a)
#ValueError

#def moje_funkce (x,y)
#    assert x is int
#    assert len(y)>0
#SyntaxError - chybí ":"

cislo = 3
pole = [1,0,2]

# for i in range(4):
#     try:
#         result = cislo/pole[i]
#     except ZeroDivisionError:
#         print("Tady delime nulou")
#         continue
#     print(f"Result is: {result}")
#IndexError