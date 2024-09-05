from datetime import datetime

def pust_v_rozpeti(from_, to_):
    def dek(func):
        def wrapper(*args, **kvargs):
            if from_ <= datetime.now().hour < to_:
                func(*args, **kvargs)
        return wrapper
    return dek


@pust_v_rozpeti(9,19)
def pozdrav():
    print("Hello world")

pozdrav()

@pust_v_rozpeti(15, 20)
def pozdrav(name):
   print(f"Hello, {name}")

pozdrav("Mark")
