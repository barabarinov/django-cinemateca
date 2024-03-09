from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from crew.admin import ActorAdmin, DirectorAdmin
from crew.models import Actor, Director


class ActorAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.actor_admin = ActorAdmin(Actor, self.site)

    def test_actor_admin_list_filter(self):
        expected_list_filter = [
            "birthday",
            "country",
        ]
        self.assertEqual(self.actor_admin.list_filter, expected_list_filter)

    def test_actor_admin_search_fields(self):
        expected_search_fields = [
            "first_name",
            "last_name",
        ]
        self.assertEqual(self.actor_admin.search_fields, expected_search_fields)


class DirectorAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.director_admin = DirectorAdmin(Director, self.site)

    def test_director_admin_search_fields(self):
        expected_search_fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
        self.assertEqual(self.director_admin.search_fields, expected_search_fields)
