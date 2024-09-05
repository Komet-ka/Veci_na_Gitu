from Dataclass import Obdelnik
from copy import deepcopy

p1 = Obdelnik(3, 4)
lst = [1, p1, 3]
no_copy_lst = lst
shallow_copy_lst = list(lst)
deep_copy_lst = deepcopy(lst)

lst[0] = 5
lst[1].a = 5
print(lst)
print(no_copy_lst)
print(shallow_copy_lst)
print(deep_copy_lst)