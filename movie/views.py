from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

# Create your views here.
from . import models


def selected_movie(request, title):
    movie = models.Movie.objects.get(title)[:20]
    return render(request, 'movie/', {
        'movies': movie
    })


def all_movies(request):
    title = request.GET.get('title')
    if title:
        movies = models.Movie.objects.filter(title__contains=title)[:20]
    else:
        movies = models.Movie.objects.all()[:20]

    return render(request, 'movie/all_movies.html', {
        'movies': movies,
        'title': title,
    })


def movie_details(request, id):
    found_movie = models.Movie.objects.get(pk=id)
    return render(request, 'movie/movie_details.html', {
        'movie': found_movie
    })
