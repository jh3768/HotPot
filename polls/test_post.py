#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User

from django.test.client import RequestFactory





class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary2@gmail.com', 'temporary2@gmail.com', 'temporary2')
        self.c = Client()
        self.login = self.c.login(username='temporary2@gmail.com', password='temporary2')
        #self.client = Client()

    def test_post(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        


        post_info= {'name': "Intro to algorithm", 'price':200, 'description' : "text book for the algorithms"}
        info= self.c.post ('/polls/profile', post_info)
        print (info)

        price = request.POST.get('price')
        description = request.POST.get('description')
        username = request.user.username
        Product.objects.create(name="Intro to algorithm", price=200, description= "text book for the algorithms")
        q = Product.objects.get(name= "Intro to algorithm", price =200)

        self.assertEqual(q.name,  "Intro to algorithm")
        self.assertEqual(q.price,  200)
        self.assertEqual(q.description, "text book for the algorithms")


      



