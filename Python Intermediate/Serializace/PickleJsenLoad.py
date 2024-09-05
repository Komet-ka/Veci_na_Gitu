import json

with open("students.json") as in_file:
    data = json.load(in_file)

print(data[0]['name'])

# data["dogs"][0]["id"]