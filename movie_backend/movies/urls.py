from django.urls import path
from . import views

urlpatterns = [
    path("trending/", views.trending_movies, name="trending-movies"),
    # add more movie endpoints here later
]
