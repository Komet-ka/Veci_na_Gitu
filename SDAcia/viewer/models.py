from django.db.models import (
  DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
  Model, TextField
)
import datetime

class Znacka(Model):
  name = CharField(max_length=128)

  def __str__(self):
    return f'{self.name}'

class Karoserie(Model):
  name = CharField(max_length=128)

  def __str__(self):
    return f'{self.name}'


class Auto(Model):
    name = CharField(max_length=128, default="")
    znacka = ForeignKey(Znacka, on_delete=DO_NOTHING)
    karoserie = ForeignKey(Karoserie, on_delete=DO_NOTHING)
    vykon = IntegerField(default=100)
    rok_vyroby = DateField(default=datetime.date.today)
    description = TextField(default="")
    price = IntegerField(default=0)
    datum_inzeratu = DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return f'Toto je Inzerát: {self.name}'


class Komentar(Model):
  name = CharField(max_length=128, default="")
  uzivatel = CharField(max_length=128, default="")
  komentar = TextField(default="")
  auto = ForeignKey(Auto, on_delete=DO_NOTHING, default="")
  datum_komentare = DateTimeField(default=datetime.datetime.now)

  def __str__(self):
    return f'Toto je Komentář s názvem: {self.name}'