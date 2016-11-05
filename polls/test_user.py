#tests.py
#import models
from django.test import TestCase
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/manufacturers/', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context['email'], 'temporary@gmail.com')
