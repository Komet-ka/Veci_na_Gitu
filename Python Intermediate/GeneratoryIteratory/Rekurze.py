def faktorial(x):
    fakt = 1
    for i in range(1, x +1):
        fakt = fakt * i
    return fakt

print(faktorial(6))

def faktorial_rek(x):
    if x == 1:
        return 1
    else:
        return x * faktorial_rek(x-1)

# x * faktorial_rek(x-1)
# x * x-1 * faktorial_rek(x-2)
# x * x-1 * x-2 * faktorial_rek(x-3)
print(faktorial_rek(100))