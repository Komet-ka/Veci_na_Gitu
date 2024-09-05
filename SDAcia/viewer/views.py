
from django.http import HttpResponse

from viewer.models import Znacka, Karoserie, Komentar, Auto

from django.shortcuts import render

def hello(request):
  return HttpResponse('Hello, world!')


def inzeraty(request):
  return render(
    request, template_name='landing_page.html',
    context={'auta': Auto.objects.all}
  )

def inzerat(request, auto_pk):
  if "komentar" in request.POST:
    new_komentar = Komentar()
    new_komentar.name = request.POST.get("name", "")
    new_komentar.uzivatel = request.POST.get("uzivatel", "")
    new_komentar.komentar = request.POST.get("komentar", "")
    new_komentar.auto = Auto.objects.get(pk=auto_pk)
    new_komentar.save()
    pass

  return render(
    request, template_name='inzerat.html',
    context={'auto': Auto.objects.get(pk=auto_pk),
             'komentare': Komentar.objects.filter(auto__pk=auto_pk)}
  )

def novy_inzerat(request):
  if "description" in request.POST:
    znacka = request.POST.get("znacka", "")
    karoserie = request.POST.get("typ karoserie", "")
    new_auto = Auto()
    new_auto.name = request.POST.get("name", "")
    new_auto.description = request.POST.get("description", "")
    new_auto.price = int(request.POST.get("price", 0))
    new_auto.rok_vyroby = int(request.POST.get("rok_vyroby", 0))
    new_auto.vykon = int(request.POST.get("vykon", 0))
    new_auto.znacka = Znacka.objects.get(pk=znacka)
    new_auto.karoserie = Karoserie.objects.get(pk=karoserie)
    new_auto.save()

  return render(
    request, template_name='novy_inzerat.html')

from django.views.generic import FormView

from viewer.forms import AutoForm
from viewer.models import Auto


class AutoCreateView(FormView):
  template_name = 'form.html'
  form_class = AutoForm

