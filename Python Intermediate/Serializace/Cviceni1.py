from json import load

def prumer(*args):
    return sum(args)/len(args)

with open("Data", "r") as f:
    data = load(f)
    print(data.keys())
    print(prumer(*data["prava_strana"]))
    print(prumer(*data["leva_strana"]))
    print(prumer(*data["prava_strana"], *data["leva_strana"]))
