def get_avg(*args):
    new_args = [x for x in args if type(x) == int or type(x) == float]
    return sum(new_args) / len(new_args)

def get_avg(*args):
    x = []
    for arg in args:
        if type(arg) == int or type(arg) == float:
            x.append(arg)
    # y = tuple(x)
    return sum(x) / len(x)

def get_avg(*args):
    x = []
    for i in range(len(args)):
        if type(args[i]) == int or type(args[i]) == float:
            x.append(args[i])
    # y = tuple(x)
    return sum(x) / len(x)

print(get_avg(1, 3.0, 'a'))