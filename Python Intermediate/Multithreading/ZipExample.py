a = ['a', 'b', 'c']
b = list(range(3))

for x, y in zip(a, b):
    print(f"x: {x}, y: {y}")

print("******")
print("vnorena verze:")
for x in a:
    for y in b:
        print(f"x: {x}, y: {y}")