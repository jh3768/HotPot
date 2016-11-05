#tests.py
#import models
from django.test import TestCase, TransactionTestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        print (User.objects.values_list('username', flat=True))
        
        #self.client = Client()

    def test_secure_page(self):
        self.client.login(username='temporary@gmail.com', password='temporary')
        response = self.client.get('/profile/', follow=True)
        newuser = User.objects.get(username='temporary@gmail.com')
        print (response.context)
        print (newuser)
        print (self.user)
        self.assertEqual(newuser, 'temporary@gmail.com')
        #self.assertEqual(response.context['E'], 'temporary@gmail.com')



