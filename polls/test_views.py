#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        
       self.c = Client()
        
        #self.client = Client()

    def test_about_status(self):
        response = self.c.get('/polls/about/', follow=True)
        self.assertEqual(response.status_code, 200)

    
    
    def test_homepage_status(self):
        response = self.c.get('/polls/', follow=True)
        self.assertEqual(response.status_code, 200)


