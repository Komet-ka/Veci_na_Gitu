import os
os.system("python ./manage.py makemigrations")
os.system("python ./manage.py migrate")

from viewer.models import Movie, Genre

"""
https://github.com/alifuk/CZ21
"""