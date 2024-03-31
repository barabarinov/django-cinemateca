from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from movie.admin import MovieAdmin, GenreAdmin, CountryAdmin
from movie.models import Movie, Genre, Country


class MovieAdminTest(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.movie_admin = MovieAdmin(Movie, self.site)

    def test_movie_admin_list_display(self):
        expected_list_display = [
            "title",
            "description",
            "year",
            "photo",
            "created_at",
            "trailer_url",
        ]
        self.assertEqual(self.movie_admin.list_display, expected_list_display)

    def test_movie_admin_list_filter(self):
        expected_list_filter = [
            "title",
            "year",
        ]
        self.assertEqual(self.movie_admin.list_filter, expected_list_filter)

    def test_movie_admin_search_fields(self):
        expected_search_fields = [
            "title",
            "year",
        ]
        self.assertEqual(self.movie_admin.search_fields, expected_search_fields)


class GenreAdminTest(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.genre_admin = GenreAdmin(Genre, self.site)

    def test_genre_admin_list_filter(self):
        expected_list_filter = [
            "title",
        ]

        self.assertEqual(self.genre_admin.list_filter, expected_list_filter)

    def test_genre_admin_search_fields(self):
        expected_search_fields = [
            "title",
        ]

        self.assertEqual(self.genre_admin.search_fields, expected_search_fields)


class CountryAdminTest(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.country_admin = CountryAdmin(Country, self.site)

    def test_country_admin_list_filter(self):
        expected_list_filter = [
            "name",
        ]

        self.assertEqual(self.country_admin.list_filter, expected_list_filter)

    def test_country_admin_search_fields(self):
        expected_search_fields = [
            "name",
        ]

        self.assertEqual(self.country_admin.search_fields, expected_search_fields)
