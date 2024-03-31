from django.urls import path

from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
)

app_name = "movie"

urlpatterns = [
    path("", MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("create/", MovieCreateView.as_view(), name="movie-create"),
    path("update/<int:pk>/", MovieUpdateView.as_view(), name="movie-update"),
    path("delete/<int:pk>/", MovieDeleteView.as_view(), name="movie-delete"),
]
