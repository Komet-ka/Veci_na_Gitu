from functools import reduce

items = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 == 1, items))
print(odds)

items = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2, items))
print(odds)

print([x for x in items if x % 2 == 1])

def pavel(x):
    return x % 2 == 1

pavel = lambda x: x % 2 == 1
odds = list(filter(pavel, items))
print(odds)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print(squared)

print([x**2 for x in items])

squared = map(lambda x: x ** 2, items)
print(squared)

# nutne pretypovani z map objectu
squared = list(map(lambda x: x ** 2, items))
print(squared)

items = [1, 2, 3, 4, 5]
items_sum = reduce(lambda x, y: x + y, items)  # 15
print(items_sum)
# [3, 3, 4, 5]
# [6, 4, 5]
# [10, 5]
# 15

items = [1, 2, 3, 4, 5]
items_sum = reduce(lambda x, y: y, items)  # 15
(print(items_sum))

# [2, 3, 4, 5]
# [3, 4, 5]
# [4, 5]
# [5]



a = [list(range(3)),['a', 'b'],list(range(3))]
print(a)
b = reduce((lambda x, y: x+y),a)
print(b)
c = list(map((lambda x: x[-1]),a))
print(c)

a = [list(range(3)),[10, 20],list(range(3))]
print(a)
print(sum(list(map(lambda x: sum(x), a))))

pairs = [(1, 10), (2, 9), (3, 8)]
pairs_sorted = sorted(pairs, key=lambda x: x[1])

print(pairs_sorted)

a = min(pairs)  # (1, 10)
a = min(pairs, key=lambda x: x[1] )
a = max(pairs)
a = max(pairs, key=lambda x: x[1])  # (1, 10)
a = max(pairs, key=lambda x: x[0] * x[1])
print(a)

print(sorted([0, 3, 6, 4, 1], reverse = True))
print(sorted([0, 3, 6, 4, 1]))