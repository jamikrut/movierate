from django.shortcuts import render

# Create your views here.
from . import models


def all_movies(request):
    movies = models.Movie.get_all()
    return render(request, 'movie/all_movies.html', {
        'movies': movies
    })


def movie_details(request, tmdb_id):
    found_movie = models.Movie.get_movie_by_tmdb_id(tmdb_id)
    return render(request, 'movie/movie_details.html', {
        'movie': found_movie
    })
