#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User
from polls.views import user_exists

class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        self.c = Client()
        self.login = self.c.login(username='temporary@gmail.com', password='temporary')
        #self.client = Client()

    def test_login(self):
        self.user = User.objects.get(username='temporary@gmail.com')
        self.assertTrue(self.login)
        self.assertEqual(self.user.username, 'temporary@gmail.com')
        self.assertEqual(self.user.email, 'temporary@gmail.com')


    def test_user_auth(self):
        self.assertIn('_auth_user_id', self.c.session)


    def test_login_status(self):
        response = self.c.get('/polls/login/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_about_status(self):
        response = self.c.get('/polls/about/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_homepage_status(self):
        response = self.c.get('/polls/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_exists(self):
        user = self.user
        self.assertTrue(user_exists(user))

    def test_user_not_exists(self):
        user =  "mock"
        self.assertFalse(user_exists(user))