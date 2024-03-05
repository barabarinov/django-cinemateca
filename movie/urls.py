from django.urls import path

from .views import index

urlpatterns = [
    path('movies/', index, name="movie-list"),
]
