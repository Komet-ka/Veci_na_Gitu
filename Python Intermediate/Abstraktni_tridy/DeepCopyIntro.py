
a = 5
b = a
a = 0
print(f"a: {a}, b: {b}")

a = [0, 5]
b = a
a[0] = 100
print(f"a: {a}, b: {b}")

a = [0, 5]
b = list(a)
a[0] = 100
print(f"a: {a}, b: {b}")

a = "asdf"
b = a
a = 'Gasdf'
print(f"a: {a}, b: {b}")