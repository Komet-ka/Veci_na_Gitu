# def prumer(*args):
#     return (sum(args))
#
#
# a = (5, 2, 3)
#
# print(prumer(*a))

def get_avg(*args):
    x = []
    for i in range(len(args)):
        if type(args[i]) == int or type(args[i]) == float:
            x.append(args[i])
    return sum(x) / len(x)


print(get_avg(1, 3, 'a'))
print(get_avg(2.4, 7, "s", 2.36))