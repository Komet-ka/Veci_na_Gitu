import re

text = "Thomas S. (33 l.), last seen in Krakow"
pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+) l\.\)"
match = re.search(pattern, text)
print(match)
print(match.groups())
print(match.group(0))
print(match.group(1))
print(match.group(2))

text = "Thomas (33) and Eva (24) agreed to go shopping together tomorrow"
pattern = r"([A-Z]{1}[a-z]+) \((\d+)\)"
print(re.findall(pattern, text))

pattern = r"a(la){4}"
text = "Ola zpivala alalala alalalala"
print(text)
print(re.findall(pattern, text))

m = re.search(pattern, text)
print(m)
print(m.group(0))
print(m.group(1))
print(m.groups())