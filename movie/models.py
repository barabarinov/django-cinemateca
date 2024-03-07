from django.db import models

from config import settings
from crew.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(default="No description")
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="movie_photos", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    trailer_url = models.URLField(null=True, blank=True)
    director = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )
    actors = models.ManyToManyField(
        to=Actor,
        related_name="movies",
    )
    genre = models.ManyToManyField(
        to="Genre",
        related_name="movies",
    )
    country = models.ManyToManyField(
        to="Country",
        related_name="movies",
    )

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "countries"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "countries"
        ordering = ["name"]

    def __str__(self):
        return self.name
