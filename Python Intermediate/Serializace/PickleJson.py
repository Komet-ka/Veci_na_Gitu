import json

students = [
    {
        'name': "John",
        'surname': "Smith",
        'score': 20
    },
    {
        'name': "Kevin",
        'surname': "Scoot",
        'score': 17
    }
]

with open("students.json", 'w') as out_file:
    json.dump(students, out_file, indent=2)