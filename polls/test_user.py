#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        self.c = Client()
        print (User.objects.values_list('username', flat=True))
        
        #self.client = Client()

    def test_secure_page(self):
        login = self.c.login(username='temporary@gmail.com', password='temporary')
        response = self.c.get('/polls/profile/', follow=True)
        self.user = User.objects.get(username='temporary@gmail.com')
        self.assertTrue(login)
        self.assertEqual(self.user.username, 'temporary@gmail.com')
        self.assertEqual(self.user.email, 'temporary@gmail.com')
        self.assertEqual(response.status_code, 200)



