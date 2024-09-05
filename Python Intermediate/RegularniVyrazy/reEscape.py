import re

# \d = [0-9]
pattern = r"\d\d \d\d"
text = "1345 Pavel ahoj 12 34 zase nejaky text 34 34"
#print(text)
#print(re.findall(pattern, text))

# \s jakakoli mezera
pattern = r"\d\d\s\d\d"
text = "13  45 Pavel ahoj 12   34 zase nejaky text 34 34"
#print(text)
#print(re.findall(pattern, text))

# \w = [A-Za-z0-9_]
pattern = r"\w+"
text = "pavel_neco_A ktery 234 09abc 09-df"
#print(text)
#print(re.findall(pattern, text))

# \S = ^\s
pattern = r"\S"
text = "pavel_neco_A ktery 234 09abc 09-df"
#print(text)
#print(re.findall(pattern, text))

# \D \S \W=  negace \d \s \w
pattern = r"\S"
text = "pavel_neco_A ktery. 234 09abc 09-df ?"
#print(text)
#print(re.findall(pattern, text))

# \.
pattern = r"ktery\."
text = "pavel_neco_A ktery. 234 09abc 09-df ?"
#print(text)
#print(re.findall(pattern, text))

# \.
pattern = r"\?"
text = "pavel_neco_A ktery. 234 09abc 09-df ?"
#print(text)
#print(re.findall(pattern, text))

# \\
pattern = r"\\"
text = "pavel_neco_A \ktery. 234 \ 09abc 09-df ?"
#print(text)
#print(re.findall(pattern, text))