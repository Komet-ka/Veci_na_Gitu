def dekorator_simple(func):
    def wrapper(*args, **kwargs):
        return_of_func = func(*args, **kwargs)
        return(return_of_func)
    return wrapper

def funkce_vracejici_dekorator(a):
    def dekorator_simple(func):
        def wrapper(*args, **kwargs):
            return_of_func = func(*args, **kwargs)
            return (return_of_func)
        return wrapper
    return dekorator_simple