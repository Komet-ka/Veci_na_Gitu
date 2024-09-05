import re

pattern = r".la"
text = ("Ola ktera jedla chleba šla domů Olga Olgga, Ela")
print(text)

def tiskni(pattern):
    text = ("Ola ktera jedla chleba šla domů Olga Olgga, Ela ale aaale dale -la abcle <to serve> First Name: Anna Last Name: Karenina\n First Name: Bob Last Name: Jones")
    print(re.findall(pattern, text))

pattern = r"Olg?a"
tiskni(pattern)

pattern = f"a+le"
tiskni(pattern)

pattern = f"a*le"
tiskni(pattern)

pattern = f"<.*?>"
tiskni(pattern)

pattern = f"[OAE]la"
tiskni(pattern)

pattern = r"a "
tiskni(pattern)

pattern = r"[a-ž]la"
tiskni(pattern)

pattern = r"[a-]la"
tiskni(pattern)

pattern = r"First Name: (.*) Last Name: (.*)"
tiskni(pattern)

# složené závorky pro opakování
pattern = r"a(la){1,3}"
text = "Ola zpivala alalala alalalala"
# print(text)
# print(re.findall(pattern, text))

# složené závorky pro opakování
pattern = r"la{2,4}"
text = "asdf Olaa laaaaa, la"
print(text)
print(re.findall(pattern, text))

# ^ negace
pattern = r"[^OA]la"
text = "Ola ktera jedla chleba šla domů Olga Olgga, Ala, Ela"
#print(text)
#print(re.findall(pattern, text))

# | nebo
pattern = r"Ala má (psa|kočku)"
text = "Ola má kočku, Ala má psa, Ala má levharta, Ala má kočku"
#print(text)
#print(re.findall(pattern, text))

# ^ jako počátek
pattern = r"^Ola"
text = "Ola má kočku, Ola má psa, Ola má levharta, Ala má kočku"
#print(text)
#print(re.findall(pattern, text))

# $ konec
pattern = r"Ola$"
text = f"""Ola má kočku, Ola má psa, Ola má levharta, Ala má kočku
Ola má psa.
Ola má kočku.
Igor šel domů a za ním šla Ola
Nevěděla kam jde"""
#print(text)
#print(re.findall(pattern, text))