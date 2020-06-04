from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Tests creating an user with an email is successful"""
        email = 'vici@nyaaa.com'
        password = 'ciocolata'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests that the email for a new user is normalized"""
        email = 'vici@CROCOBAUR.COM'
        user = get_user_model().objects.create_user(
            email,
            'miau'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'vici@picutamea.com',
            'ciacarlaci'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
