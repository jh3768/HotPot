#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        self.c = Client()
        #self.client = Client()

    def test_login(self):
        login = self.c.login(username='temporary@gmail.com', password='temporary')
        self.user = User.objects.get(username='temporary@gmail.com')
        self.assertTrue(login)
        self.assertEqual(self.user.username, 'temporary@gmail.com')
        self.assertEqual(self.user.email, 'temporary@gmail.com')


    def test_user_auth(self):
        self.assertIn('_auth_user_id', self.c.session)


    def test_login_status(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
