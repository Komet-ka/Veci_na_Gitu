import re

# text = "48123456789asdf, +48123456789, asdf, 0048123456789"
# pattern = r"[48,0048,\+48]\d{9}"
# tuple = re.findall(pattern, text)
# for polozka in tuple:
#     print(polozka)
#
# print(".......................................")

text = "48123456789asdf, +48123456789, asdf, 0048123456789, 123456, 00048123456789"
pattern = r","
seznam = re.split(pattern, text)
print(seznam)

for polozka in seznam:
    pattern = r"48\d{9}"
    if bool(re.search(pattern, polozka)):
        print(re.findall(pattern, polozka), True)
    else:
        print(polozka, False)