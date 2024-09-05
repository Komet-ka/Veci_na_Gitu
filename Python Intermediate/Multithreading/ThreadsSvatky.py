import requests

a = requests.get("https://svatky.adresa.info/json?name=Pavel")
print(a.text)

a = requests.get("https://svatky.adresa.info/json?date=2906")
print(a.text)