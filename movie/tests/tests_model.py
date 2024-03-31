from django.test import TestCase
from django.contrib.auth import get_user_model

from movie.models import Movie, Genre, Country
from crew.models import Actor


class MovieModelTest(TestCase):

    def setUp(self):
        self.director = get_user_model().create_user(
            username="director",
            password="testpassword",
        )
        self.actor = Actor.objects.create(
            first_name="Actor Name",
            last_name="Actor Lastname",
            birthday="1980-01-01",
        )
        self.genre = Genre.objects.create(title="Comedy")
        self.country = Country.objects.create(name="USA")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            year=2020,
            director=self.director,
        )
        self.movie.actors.add(self.actor)
        self.movie.genres.add(self.genre)
        self.movie.countries.add(self.country)

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.description, "Test Description")
        self.assertEqual(self.movie.year, 2020)
        self.assertEqual(self.movie.director, self.director)
        self.assertIn(self.actor, self.movie.actors.all())
        self.assertIn(self.genre, self.movie.genres.all())
        self.assertIn(self.country, self.movie.countries.all())

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")


class GenreModelTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(title="Thriller")

    def test_genre_creation(self):
        self.assertEqual(self.genre.title, "Thriller")

    def test_genre_str(self):
        self.assertEqual(str(self.genre), "Thriller")


class CountryModelTest(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Canada")

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Canada")

    def test_country_str(self):
        self.assertEqual(str(self.country), "Canada")
