import csv

from django.db import models


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
