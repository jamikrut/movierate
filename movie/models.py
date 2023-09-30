import csv

from django.db import models


# Create your models here.

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
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return f'{self.title}, {self.release_date}'

    @staticmethod
    def get_all():
        movies_arr = []

        with open('movie/movies_small.csv', 'r', encoding='utf-8') as input_file:
            input_file.readline()
            reader = csv.reader(input_file, delimiter=',')

            for row in reader:
                movies_arr.append(Movie(row[1], row[5], row[6], row[7], row[8], row[10],
                                        row[11], row[12], row[13], row[14], row[15], row[16], row[17], ))

        return movies_arr

    @staticmethod
    def get_movie_by_tmdb_id(tmdb_id):
        all_movies = Movie.get_all()
        for movie in all_movies:
            if movie.tmdb_id == tmdb_id:
                return movie

        return None
