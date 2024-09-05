from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea
)

from viewer.models import Znacka, Karoserie

class AutoForm(Form):

  name = CharField(max_length=128)
  znacka = ModelChoiceField(queryset=Znacka.objects)
  karoserie = ModelChoiceField(queryset=Karoserie.objects)
  vykon = IntegerField(min_value=100, max_value=500)
  rok_vyroby = DateField()
  description = CharField(widget=Textarea, required=False)
  price = IntegerField()