from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from movies.services.tmdb import TMDbClient

client = TMDbClient()


@api_view(["GET"])
@permission_classes([AllowAny])
def discover_movies(request):
    sort_by = request.query_params.get("sort_by", "popularity.desc")
    min_rating = request.query_params.get("min_rating")

    data = client.discover_movies(
        sort_by=sort_by,
        min_vote_average=float(min_rating) if min_rating else None,
    )
    return Response(data)


@api_view(["GET"])
@permission_classes([AllowAny])
def search_movies(request):
    query = request.query_params.get("q")
    if not query:
        return Response(
            {"error": "Query parameter 'q' is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    data = client.search_movies(query=query)
    return Response(data)


@api_view(["GET"])
@permission_classes([AllowAny])
def movie_details(request, movie_id: int):
    append = request.query_params.get("append_videos") == "true"
    data = client.get_movie_details(movie_id, append_videos=append)
    return Response(data)


@api_view(["GET"])
@permission_classes([AllowAny])
def movie_videos(request, movie_id: int):
    data = client.get_movie_videos(movie_id)
    return Response(data)
