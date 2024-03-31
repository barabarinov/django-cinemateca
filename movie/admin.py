from django.contrib import admin
from django.contrib.admin import ModelAdmin

from movie.models import Movie, Genre, Country


@admin.register(Movie)
class MovieAdmin(ModelAdmin):
    list_display = [
        "title",
        "description",
        "year",
        "photo",
        "created_at",
        "trailer_url",
    ]
    list_filter = [
        "title",
        "year",
    ]
    search_fields = [
        "title",
        "year",
    ]


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_filter = [
        "title",
    ]
    search_fields = [
        "title",
    ]


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_filter = [
        "name",
    ]
    search_fields = [
        "name",
    ]
