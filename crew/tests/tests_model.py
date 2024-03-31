from django.contrib.auth import get_user_model
from django.test import TestCase

from crew.models import Director, Actor
from movie.models import Country


class DirectorActorModelTest(TestCase):

    @staticmethod
    def create_country(name="Some Country"):
        return Country.objects.create(name=name)

    def create_director(
        self,
        username="director",
        password="Istanbul1996",
        first_name="John",
        last_name="Doe",
        birthday="1980-01-01",
    ):
        country = self.create_country()

        return get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            country=country,
        )

    def create_actor(self, first_name="Jane", last_name="Doe", birthday="1990-01-01"):
        country = self.create_country(name="Actorland")

        return Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            country=country,
        )

    def test_director_creation(self):
        director = self.create_director()

        self.assertTrue(isinstance(director, Director))
        self.assertEqual(str(director), "John Doe")
        self.assertTrue(director.check_password("Istanbul1996"))

    def test_actor_creation(self):
        actor = self.create_actor()

        self.assertTrue(isinstance(actor, Actor))
        self.assertEqual(str(actor), "Jane Doe")
