#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from polls.views import post, delete
from polls.models import Product
from polls.views import auth_and_signup
from django.contrib.sessions.middleware import SessionMiddleware

class TestUser(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('temporary4@gmail.com', 'temporary4@gmail.com', 'temporary4')
        self.login = self.c.login(username='temporary4@gmail.com', password='temporary4')
        self.singupinfo = {'password': 'temporary4', 'email': 'temporary4@gmail.com'}
        self.singupinfo2 = {'password': 'temporary5', 'email': 'temporary5@gmail.com'}
        self.singupinfo3 = {'password': 'temporary2000', 'email': 'temporary2000@gmail.com'}
        self.factory = RequestFactory()

    def test_signup(self):   
        self.user = User.objects.get(username='temporary4@gmail.com')
        self.assertTrue(self.login)
        self.assertEqual(self.user.username, 'temporary4@gmail.com')
        self.assertEqual(self.user.email, 'temporary4@gmail.com')


    def test_user_auth(self):
        self.assertIn('_auth_user_id', self.c.session)

    def test_signup_status(self):
        self.login = self.c.login(username='temporary4@gmail.com', password='temporary4')
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_and_signup_status(self):
        "test if the above user is auth_and_login_"
        request = self.factory.post('/polls/login/', data = self.singupinfo)
        response= auth_and_signup(request)
        self.assertEqual(response.status_code, 302)

    def test_auth_and_signup_status2(self):
        "test if the above user is auth_and_login_"
        request = self.factory.post('/polls/login/', data = self.singupinfo2)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        response = auth_and_signup(request)
        self.assertEqual(response.status_code, 302)

    def test_auth_and_signup_status3(self):
        "test if the above user is auth_and_login_"
        request = self.factory.post('/polls/login/', data = self.singupinfo3)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        response = auth_and_signup(request)
        self.assertEqual(response.status_code, 302)


    def teardown(self):
        User.objects.filter(email = "temporary4@gmail.com").delete()
        User.objects.filter(email = "temporary5@gmail.com").delete()
        User.objects.filter(email = "temporary2000@gmail.com").delete()