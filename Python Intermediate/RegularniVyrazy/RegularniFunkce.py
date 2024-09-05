import re

print(re.findall(r".la", "Ola ala Ela"))

p = re.compile(r".la")
print(p.findall("Ola ala Ela"))
print(p.match("Ola ala Ela"))

print(re.findall(r".la", "Ola ala Ela"))

iter = re.finditer(r".la", "Ola ala Ela")

for elem in iter:
    print(elem)

#pokus = re.finditer(r".la", "Ola ala Ela")
#print(list(pokus))

#print([x.span() for x in list(pokus) ])

print(re.fullmatch(r"[A-Z]la", "Ela"))

# equivalent
print(re.search(r"^[A-Z]la$", "Ela"))

print(re.match(r"[A-Z]la", "ala Ola Ela"))
print(re.match(r"[a-z]la", "ala Ola Ela"))
print(re.search(r"^[A-Z]la", "ala Ola Ela"))

m = re.search(r"[A-Z]la", "ala Ola Ela")
print(m)

print(m.span()[0])
print(m.group())

m = re.search(r"[A-Z]la", "ala ola ela")
print(m)
print(m.group())

pattern = r",|\."
text = "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"
print(re.split(pattern, text))

pattern = r"ovoce,"
text = "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"
print(re.split(pattern, text))

print(re.sub(r"[a-z]{5}", "pes", "Alice má slona"))

print(re.subn(r"[a-z]{5}", "pes", "Alice má slona"))

print(re.subn(r"[a-z]{4}", "pes", "Alice má slona"))

