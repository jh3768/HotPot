#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('temporary4@gmail.com', 'temporary4@gmail.com', 'temporary4')
        self.login = self.c.login(username='temporary4@gmail.com', password='temporary4')
        

    def test_signup(self):   
        self.user = User.objects.get(username='temporary4@gmail.com')
        self.assertTrue(self.login)
        self.assertEqual(self.user.username, 'temporary4@gmail.com')
        self.assertEqual(self.user.email, 'temporary4@gmail.com')


    def test_user_auth(self):
        self.assertIn('_auth_user_id', self.c.session)


    def test_signup_status(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
