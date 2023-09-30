from django.shortcuts import render

# Create your views here.
from . import models


def all_movies(request):
    movies = models.Movie.get_all()
    return render(request, 'movie/all_movies.html', {
        'movies': movies
    })
