cislo = 3
pole = [1,0,2]

for i in pole:
    if i == 0:
        raise ValueError("Nemuzes delit nulou")
    result = cislo/i
    print(f"Result is: {result}")