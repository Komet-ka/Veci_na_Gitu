from copy import deepcopy


lst = [1, {'a': 1, 'b': [2, 4, 5]}, 3]
plytka_kopie_lst = list(lst)
hluboka_kopie_lst = deepcopy(lst)

lst[0] = 5
lst[1]['a'] = 5
print(lst)
print(plytka_kopie_lst)
print(hluboka_kopie_lst)

a = []
a.append(5)
print(a)

a = list(range(5))
a.append(5)
print(a)