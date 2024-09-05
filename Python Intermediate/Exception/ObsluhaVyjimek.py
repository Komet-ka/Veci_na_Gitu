try:
    a = 2
    b = 1
    # assert a == b

    #pole = 3,5
    #pole.append(6)

    # pole = [3,5]
    # print(pole[4])

    # a = 5/0

    #f = open("text.txt")

    #test = a + b + "ahoj"

    #import utils2

    x = 10
    if x == 10:
        print("x je 10")
    else:
        print("x není 10")


except AssertionError:
    print("podařil se mi AssertionError")
except AttributeError:
    print("Podařil se mi AttributeError!")
except IndexError:
    print("Podařil se mi IndexError!")
except ZeroDivisionError:
    print("podařil se mi ZeroDivisionError")
except NameError:
    print("podařil se mi NameError")
except TypeError:
    print("podařil se mi TypeError")
except ImportError:
    print("Podařil se mi ImportError!")
except FileNotFoundError:
    print("Podařil se mi FileNotFoundError!")
except (ValueError, KeyError):
    print("podařil se mi ValueError nebo KeyError")
finally:
    print("Gratuluji, dostal ses až na konec kodu")