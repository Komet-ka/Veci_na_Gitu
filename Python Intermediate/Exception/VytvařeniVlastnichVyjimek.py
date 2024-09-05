class CustomException(Exception):
    def __init__(self):
        message = "The divisor cannot be zero"
        super().__init__(message)


a = 3
b = [1, 0, 2]
for elem in b:
    try:
        result = a / elem
    except ZeroDivisionError as e:
        print(e)
        print(type(e))
        print("chtěl jsem delit nulou")
        continue
    print(f"Result is: {result}")