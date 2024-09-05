from django.http import HttpResponse
from viewer.models import Genre, Movie

def zakladni(request):
  return HttpResponse(f'Jsi u sebe na localhost')


def soucet(request, a, b):
  return HttpResponse(f'Soucet cisel {a} a {b} je {int(a) + int(b)}')

def vlozeniParametruPresURL(request):
  param = request.GET.get('param', '')
  return HttpResponse(f'Parametr má hodnotu {param}')

def filtrovani():
  pass

def add_genre(request, new_name):
  genre = Genre(name = new_name)
  genre.save()
  return HttpResponse(f'Žánr {genre} přidán.')

def delete_genre(request, genre_name):
  genre = Genre.objects.get(name=genre_name)
  genre.delete()
  return HttpResponse(f'Žánr {genre_name} byl smazán.')

def edit_description(request, title, new_description):
  movie = Movie.objects.get(title=title)
  movie.description = new_description
  movie.save()
  return HttpResponse(f'Popisek se změnil.')

def count_movies(request):
  pocet = Movie.objects.count()
  return HttpResponse(f'Momentálně máte v databázi {pocet} filmů.')


from django.shortcuts import render

def hello(request, s0):
  s1 = request.GET.get('s1', '')
  return render(
    request, template_name='hello.html',
    context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
  )

def movies(request):

    return render(
    request, template_name='movies.html',
    context={'movies': Movie.objects.all,
             'Genre': Genre}
  )

def movie_filter(request):


  return render(
    request, template_name='movies.html',
    context={'movies': Movie.objects.filter(genre=genre),
             'Genre': Genre}
    )

from django.views import View
from django.views.generic import TemplateView

class MoviesView(View):
  def get(self, request):
    return render(
      request, template_name='movies.html',
      context={'movies': Movie.objects.all()}
    )
class MoviesTemplateView(TemplateView):
  template_name = 'movies.html'
  extra_context = {'movies': Movie.objects.all()}


from django.views.generic import ListView
class MoviesViewList(ListView):
  template_name = 'movies2.html'
  model = Movie

from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import UpdateView

from viewer.forms import MovieForm
from viewer.models import Movie

LOGGER = getLogger()


class MovieUpdateView(UpdateView):

  template_name = 'form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('index')

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data while updating a movie.')
    return super().form_invalid(form)