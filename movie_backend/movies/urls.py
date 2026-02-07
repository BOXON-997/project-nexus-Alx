from django.urls import path
from .views import discover_movies, search_movies, find_movie_by_external_id

urlpatterns = [
    path("discover/", discover_movies, name="discover-movies"),
    path("search/", search_movies, name="search-movies"),
    path("find/<str:external_id>/", find_movie_by_external_id, name="find-movie"),
]