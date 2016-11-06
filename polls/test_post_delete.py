from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from polls.views import post, delete
from polls.models import Product


class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary2@gmail.com', 'temporary2@gmail.com', 'temporary2')
        self.c = Client()
        self.c.login(username='temporary2@gmail.com', password='temporary2')
        self.factory = RequestFactory()
        self.product_info1 = {'name': "Intro to algorithm", 'price':200, 'description' : "text book for the algorithms"}
        self.product_info2 = {'name': "db", 'price':100, 'description' : "text book for the db"}

    def test_post(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info1)
        request.user = self.user
        response = post(request)
        
        query = Product.objects.get(name = "Intro to algorithm", price = 200)
        
        self.assertEqual(query.description, "text book for the algorithms")
        self.assertEqual(query.name, "Intro to algorithm")
        self.assertEqual(query.price, 200)
        


    def test_delete(self):
        request = self.factory.post('/polls/post/', data = self.product_info2)
        request.user = self.user
        post(request)
        
        q = Product.objects.get(name = "db", price = 100)
        self.assertTrue(Product.objects.filter(name = "db").exists())
        self.assertEqual(q.description, "text book for the db")
        
        request = self.factory.post("/polls/delete/", {'delete': "db"})
        request.user = self.user
        delete(request)
        
        self.assertFalse(Product.objects.filter(name = "db").exists())
