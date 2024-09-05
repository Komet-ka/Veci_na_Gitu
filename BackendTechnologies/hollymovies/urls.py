"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)


from viewer.views import (hello, soucet, zakladni, vlozeniParametruPresURL,
                          add_genre, delete_genre, edit_description, count_movies,
                          movies, movie_filter, MoviesView, MoviesTemplateView,
                          MoviesViewList, MovieUpdateView)

urlpatterns = [
    path("", zakladni),
    path('admin/', admin.site.urls),
    path('hello/<s0>', hello),
    path('hello', hello),
    path('soucet/<a>/<b>', soucet),
    path('vlozeniParametruPresURL', vlozeniParametruPresURL),
    path('add_genre/<new_name>', add_genre),
    path('delete_genre/<genre_name>', delete_genre),
    path('edit_description/<title>/<new_description>', edit_description),
    path('count_movies/', count_movies),
    path('movies/', movies),
    path('movie_filter/', movie_filter),
    path('index', MoviesView.as_view(), name='index'),
    path('index2', MoviesTemplateView.as_view(), name='index2'),
    path('index3', MoviesViewList.as_view(), name='index3'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update')

]
