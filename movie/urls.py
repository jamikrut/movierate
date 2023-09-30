from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name='all_movies'),
    path('<tmdb_id>', views.movie_details, name='movie_details')
]
