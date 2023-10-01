from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name='all_movies'),
    path('<int:id>', views.movie_details, name='movie_details'),
    path('collection', views.all_collections, name='all_collections'),
    path('collection/<int:id>', views.collection_details, name='collection_details'),
]
