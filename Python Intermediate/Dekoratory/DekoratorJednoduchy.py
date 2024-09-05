from datetime import datetime

def vypni_v_noci(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 18:
            func()
    return wrapper

def zapni_v_noci(func):
    def wrapper():
        if datetime.now().hour <= 7 or datetime.now().hour >= 19:
            func()
    return wrapper

@vypni_v_noci
def pozdrav1():
    print("Dobry den!")

@zapni_v_noci
def pozdrav2():
    print("Dobrou noc!")

pozdrav1()
pozdrav2()