#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User
from polls.views import user_exists, profilejson

class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        self.user1 = User.objects.create_user(username = 'temporary2@gmail.com', email = 'temporary@gmail.com', last_name = 't', first_name = 'm', password = 'temporary')
        self.c = Client()
        self.login = self.c.login(username='temporary@gmail.com', password='temporary')
        self.product_info = {'name': "Intro to algorithm", 'price':200, 'description' : "text book for the algorithms", 'username': 'temporary2@gmail.com', 'category': "books"}
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

    def test_signup_fail_status(self):
        c = Client()
        login = c.login(username='temporary1000@gmail.com', password='temporary4')
        response = self.c.get('/polls/login/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_url(self):
        login = self.c.login(username='temporary1000@gmail.com', password='temporary4')
        response = self.c.get('/polls/delete/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_url2(self):
        c = Client()
        response = c.get('/polls/delete/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        c = Client()
        response = c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        c = Client()
        response = c.get('/polls/logout/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout2(self):
        response = self.c.get('/polls/logout/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.c.get('/polls/post/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post2(self):
        c= Client()
        response = c.get('/polls/post/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_homepagejson(self):
        c= Client()
        response = c.post('/polls/homepagejson')
        self.assertEqual(response.status_code, 200)

    def test_homepagejson2(self):
        c= Client()
        response = c.post('/polls/homepagejson?category=books')
        self.assertEqual(response.status_code, 200)


    def test_profilejson(self):
    
        request= self.c.post('/polls/post', data = self.product_info)
        request.user= self.user
        response= profilejson(request)
        self.assertEqual(response.status_code, 200)

    def test_profilejson2(self):
        c= Client()
        request= c.post('/polls/post', data = self.product_info)
        self.user1.username = None
        request.user = self.user1
        response= profilejson(request)
        self.assertEqual(response.status_code, 302)

    def teardown(self):
        Product.objects.filter(name = "Intro to algorithm").delet()
