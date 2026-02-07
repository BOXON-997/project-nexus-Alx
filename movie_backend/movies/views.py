from django.shortcuts import render
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.tmdb import get_trending_movies

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Favorite


@api_view(["GET"])
def trending_movies(request):
    cache_key = "trending_movies"
    movies = cache.get(cache_key)

    if not movies:
        movies = get_trending_movies()
        cache.set(cache_key, movies, timeout=60 * 60)

    return Response(movies)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    movie_id = request.data["tmdb_id"]
    movie, _ = Movie.objects.get_or_create(tmdb_id=movie_id, defaults={
        "title": request.data.get("title", "")
    })
    Favorite.objects.get_or_create(user=request.user, movie=movie)
    return Response({"message": "Added to favorites"})