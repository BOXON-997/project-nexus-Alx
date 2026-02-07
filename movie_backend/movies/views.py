from django.shortcuts import render
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.tmdb import get_trending_movies

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Favorite


@api_view(["GET"])
@permission_classes([AllowAny])
def discover_movies(request):
    """
    Discover movies using TMDb filters.
    Defaults to trending (popularity.desc).
    """
    sort_by = request.query_params.get("sort_by", "popularity.desc")
    min_rating = request.query_params.get("min_rating")

    data = client.discover_movies(
        sort_by=sort_by,
        min_vote_average=float(min_rating) if min_rating else None,
    )
    return Response(data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    movie_id = request.data["tmdb_id"]
    movie, _ = Movie.objects.get_or_create(tmdb_id=movie_id, defaults={
        "title": request.data.get("title", "")
    })
    Favorite.objects.get_or_create(user=request.user, movie=movie)
    return Response({"message": "Added to favorites"})