from django.urls import path

from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name='movie-detail'),
    path("movies/create/", MovieCreateView.as_view(), name='movie-create'),
    path("movies/update/<int:pk>/", MovieUpdateView.as_view(), name='movie-update'),
    path("movies/delete/<int:pk>/", MovieDeleteView.as_view(), name='movie-delete'),
]
