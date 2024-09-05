nadruhou = lambda x: x**2
print(nadruhou(2))
my_lambda = lambda y: y.lower()
print(my_lambda("Ha, Ha, Ha!"))
rovna_se = lambda x, y: x==y
print(rovna_se(1,2))

equals_lambda = lambda x, y: x == y
print(equals_lambda(1, 1))

def equals(x, y):
    return x == y

print(equals(1,1))

def prvni_a_delka(x):
    return (x[0], len(x))

print(prvni_a_delka(['a', 3, 4, 6, 3]))

prvni = lambda x: (x[0], len(x))
print(prvni(['a', 3, 4, 6, 3]))

