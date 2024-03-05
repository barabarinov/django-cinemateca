from django.contrib.auth.models import AbstractUser
from django.db import models

from crew.models import Actor, Director


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(default="No description")
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="movie_photos", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    trailer_url = models.URLField(null=True)
    director = models.ForeignKey(
        to=Director,
        on_delete=models.SET_NULL,
        related_name="movies",
        null=True,
        blank=True,
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
    production = models.ForeignKey(
        to="Production",
        on_delete=models.SET_NULL,
        related_name="movies",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Production(AbstractUser):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(
        to=Country,
        on_delete=models.SET_NULL,
        related_name="productions",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.username
