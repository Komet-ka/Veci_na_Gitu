def secti_tuple(*args):
    soucet = 0
    for prvek in args:
        soucet = soucet + prvek
    return soucet

print(secti_tuple(10, 10, 1))

def vytiskni_slovnik(**kvargs):
    for k, v  in kvargs.items():
        print(f"{k}: {v}")


vytiskni_slovnik(a = 10, b = 10, c = 1)