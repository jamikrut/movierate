import csv

from django.db import models


# Create your models here.

class Movie:
    def __init__(self, tmdb_id, title, cast, homepage, director, keywords, overview, runtime_min, genres,
                 production_companies, release_date, vote_count, vote_average):
        self.tmdb_id = tmdb_id
        self.title = title
        self.cast = cast
        self.homepage = homepage
        self.director = director
        self.keywords = keywords
        self.overview = overview
        self.runtime_min = runtime_min
        self.genres = genres
        self.production_companies = production_companies
        self.release_date = release_date
        self.vote_count = vote_count
        self.vote_average = vote_average

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
