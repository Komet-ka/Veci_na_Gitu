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

Animals = {
  "ids": [
    {
      "id": 0,
      "race": "pes"
    },
    {
      "id": 1,
      "race": "pes"
    }
  ],
  "cats": [
    {
      "id": 0,
      "race": "puszek"
    },
    {
      "id": 1,
      "race": "greebo"
    }
  ],

  "dogs": [
    {
      "id": 0,
      "name": "Max",
      "race": "dog"
    },
    {
      "id": 1,
      "name": "Buddy",
      "race": "dog"
    }
  ],
  "cats": [
    {
      "id": 0,
      "name": "Whiskers",
      "race": "cat"
    },
    {
      "id": 1,
      "name": "Greebo",
      "race": "cat"
    }
  ]
}

with open("Animals.json", 'w') as out_file:
    json.dump(Animals, out_file, indent=2)