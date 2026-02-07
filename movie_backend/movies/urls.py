from django.urls import path
from .views import (
    discover_movies,
    search_movies,
    movie_details,
    movie_videos,
)

urlpatterns = [
    path("discover/", discover_movies, name="discover-movies"),
    path("search/", search_movies, name="search-movies"),
    path("movie/<int:movie_id>/", movie_details, name="movie-details"),
    path("movie/<int:movie_id>/videos/", movie_videos, name="movie-videos"),
]
