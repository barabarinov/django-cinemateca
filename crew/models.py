from django.contrib.auth.models import AbstractUser
from django.db import models


class Director(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="director_photos", null=True, blank=True
    )
    country = models.ForeignKey(
        to="movie.Country",
        related_name="directors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Directors"
        ordering = ["first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="actor_photos", null=True)
    country = models.ForeignKey(
        to="movie.Country",
        related_name="actors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
