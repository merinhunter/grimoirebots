from django.test import TestCase
from django.db import IntegrityError

from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username="vader",
            first_name="Anakin",
            last_name="Skywalker",
            email="vader@imperial.emp",
        )

    def test_user_full_name(self):
        """
        get_full_name() returns a combination of the fields first_name and
        last_name
        """
        vader = User.objects.get(username="vader")
        self.assertEqual(vader.get_full_name(), "Anakin Skywalker")

    def test_user_short_name(self):
        """
        get_short_name() returns the field first_name
        """
        vader = User.objects.get(username="vader")
        self.assertEqual(vader.get_short_name(), "Anakin")

    def test_repeated_username(self):
        """
        The field username must be unique
        """
        with self.assertRaises(IntegrityError):
            User.objects.create(username="vader")

    def test_repeated_email(self):
        """
        The field email must be unique
        """
        with self.assertRaises(IntegrityError):
            User.objects.create(email="vader@imperial.emp")
