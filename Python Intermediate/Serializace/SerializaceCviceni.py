from json import load
def prumer(*args):
    return(sum(args)/len(args))

with open('data.txt', 'r') as f:
    data = load(f)
    print(data.keys())
    print(prumer(*data['prava_strana']))
    print(prumer(*data['leva_strana']))
    print(prumer(*data['prava_strana'], *data['leva_strana']))

# druha verze syntaxe
print("")
print("")
f = open('data.txt', 'r')
data = load(f)
print(prumer(*data['prava_strana']))
print(prumer(*data['leva_strana']))
print(prumer(*data['prava_strana'], *data['leva_strana']))
f.close()

a = (1, 3, 4)
b = [1, 0, 4, 6]

print(prumer(1, 4, *a, 5, *b))