import csv

from django.db import models
from django.core.validators import MaxLengthValidator


# Create your models here.

class MovieStatistics(models.Model):
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return f'Statystyki dla filmu {self.movie.title}'


class Movie(models.Model):
    tmdb_id = models.CharField(max_length=15)
    title = models.CharField(max_length=1000)
    cast = models.CharField(max_length=1000)
    homepage = models.URLField()
    director = models.CharField(max_length=1000)
    keywords = models.CharField(max_length=1000)
    overview = models.TextField()
    runtime_min = models.IntegerField()
    genres = models.CharField(max_length=1000)
    production_companies = models.CharField(max_length=1000)
    release_date = models.DateField()
    statistics = models.OneToOneField(MovieStatistics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.release_date}'

    @staticmethod
    def create_from_form(movie_data):
        initial_statistics = MovieStatistics.objects.create(vote_count=0, vote_average=0)

        Movie.objects.create(
            tmdb_id=movie_data['tmdb_id'],
            title=movie_data['title'],
            cast=movie_data['cast'],
            homepage=movie_data['homepage'],
            director=movie_data['director'],
            keywords=movie_data['keywords'],
            overview=movie_data['overview'],
            runtime_minutes=movie_data['runtime_minutes'],
            genres=movie_data['genres'],
            production_companies=movie_data['production_companies'],
            release_date=movie_data['release_date'],
            statistics=initial_statistics
        )


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_name = models.EmailField(max_length=100)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class MovieCollection(models.Model):
    name = models.CharField(max_length=255, validators=[
        MaxLengthValidator(4)
    ])
    creation_date = models.DateField()
    update_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
