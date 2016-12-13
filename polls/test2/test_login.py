#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test.client import RequestFactory
from polls.views import post, delete
from polls.models import Product
from polls.views import auth_and_login 


class TestUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username = 'temporary@gmail.com', email = 'temporary@gmail.com', last_name = 't', first_name = 'm', password = 'temporary')
        self.user2 = User.objects.create_user(username = 'invalid_email_address', email='invalid_email_address', password = 'temporary', last_name = 't', first_name = 'm')
        self.user3 = User.objects.create_user(username = 'user3', email='', password = 'temporary', last_name = 't', first_name = 'm')
        self.user5 = User.objects.create_user(username = 'user5', email='user5@gmail.com', password = '', last_name = 't', first_name = 'm')
        self.user8 = User.objects.create_user(username = 'user8', email = 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww@wwwwwwwwwwwwwwwwwwwwwwwwwwww.com',  password = 'temporary', last_name = 't', first_name = 'm')
        self.user23 = User.objects.create_user(username = 'user23', email='user5@gmail.com', password = 'gergeogogo3ht2rh20rh2rh23r83r23hr23r2398r9hwhehf23hr203rh203hgjkegf3034h0th34th34t834ht934t3gnkergn34gh34r', last_name = 't', first_name = 'm')
        self.user12 = User.objects.create_user(username = 'temporary2@columbia.com', email = 'temporary2@columbia.com', last_name = 'temp', first_name = 'orary', password = 'temporary')
        self.user13 = User.objects.create_user(username = 'invalid_email_address2', email='no at', password = 'temporary', last_name = 't', first_name = 'm')
        self.user14 = User.objects.create_user(username = 'user14', email=' ', password = 'temporary', last_name = 't', first_name = 'm')
        self.user15 = User.objects.create_user(username = ' ', email='user15@columbia.edu', password = 'temporary', last_name = 't', first_name = 'm')
        self.user16 = User.objects.create_user(username = 'user16', email='user5@gmail.com', password = ' ', last_name = 't', first_name = 'm')
        self.user19 = User.objects.create_user(username = 'user19', email ='wfjwgh3409t3ggh4ohj4h045h04uh945hi4509hu409hu490hu490hu049h90j2oije2hr293 hrh23hr9023ur0923ur230hr2h092r023ur23rh23rh239hr2rh289h289rh2389h2389rh2rj2rh9wefwo32@gmail.com', password = 'temporary', last_name = 't', first_name = 'm')
        self.logininfo = {'password': 'temporary1000', 'email': 'temporary1000@gmail.com'}
        self.logininfo2 = {'password': 'temporary', 'email': 'temporary@gmail.com'}
        self.c = Client()
        self.factory = RequestFactory()

    def test_login_user1(self):
        self.login = self.c.login(username='temporary@gmail.com', password='temporary')
        self.user1 = User.objects.get(username='temporary@gmail.com')
        "test if a user is able to log in"
        self.assertTrue(self.login)
        "test if a user is authenticated"
        self.assertIn('_auth_user_id', self.c.session)
        "test if the user has the same passowrd and username from signup"
        self.assertEqual(self.user1.username, 'temporary@gmail.com')
        self.assertEqual(self.user1.email, 'temporary@gmail.com')
         
         
    def test_login_status1(self):
        "test if the above user is logged in"
        self.login = self.c.login(username='temporary@gmail.com', password='temporary')
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_and_login_status(self):
        "test if the above user is auth_and_login_"
        request = self.factory.post('/polls/login/', data = self.logininfo)
        response= auth_and_login(request)
        #self.assertEqual(response.status_code, 302)

    def test_auth_and_login_status2(self):
        "test if the above user is auth_and_login_"
        request = self.factory.post('/polls/login/', data = self.logininfo2)
        #auth_and_login(request)
        #self.assertEqual(response.status_code, 302)
         
   