from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from polls.views import post, delete
from polls.models import Product

class TestLoggedUser(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user('temporary2@gmail.com', 'temporary2@gmail.com', 'temporary2')
        self.user.save()
        self.client.login(username='temporary2@gmail.com', password='temporary2@gmail.com')

    def tearDown(self):
        self.user.delete()

    def test_logged_user_get_homepage(self):
        response = self.client.get(('/polls/profile'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logged_user_get_settings(self):
        response = self.client.get(('/polls'), follow=True)
        self.assertEqual(response.status_code, 200)