import datetime

from django.db import migrations
import csv
from movie.models import Movie


def load_initial_data(app, schema_editor):
    with open('movie/migrations/movies.csv', 'r', encoding='utf-8') as input_file:
        input_file.readline()
        reader = csv.reader(input_file, delimiter=',')

        for row in reader:
            movie = Movie(tmdb_id=row[1], title=row[5], cast=row[6], homepage=row[7], director=row[8], keywords=row[10],
                          overview=row[11], runtime_min=int(row[12]), genres=row[13], production_companies=row[14],
                          release_date=datetime.datetime.strptime(row[15], '%m/%d/%Y'),
                          vote_count=int(row[16]), vote_average=float(row[17]))
            movie.save()


class Migration(migrations.Migration):
    dependencies = [
        ('movie', '0003_remove_movie_name'),
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
