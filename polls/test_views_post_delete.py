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
        self.product_info3 = {'name': "db negative price", 'price':-100, 'description' : "text book for the db negative price"}
        self.product_info4 = {'name': "db2", 'price':-10, 'description' : "text book for the db2"}
        self.product_info5 = {'name': "db3", 'price':10, 'description' : ""}
        self.product_info6 = {'name': "egeorgeorgjeorgjeogjeorgjerogjeoigjeogjoejfo2jro23rongoengoengoerjgeogjeogjeogjeogjeogjeogjeogeogjeogjeogjeogjeojgoejgoejgoerjerogjerogjeogjeo", 'price':100, 'description' : "text book for the db4"}
        self.product_info7 = {'name': "abc", 'price':200, 'description' : "text book for the abc"}

    def test_post1(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info1)
        request.user = self.user
        response = post(request)
        
        query = Product.objects.get(name = "Intro to algorithm", price = 200)
        
        self.assertEqual(query.description, "text book for the algorithms")
        self.assertEqual(query.name, "Intro to algorithm")
        self.assertEqual(query.price, 200)
        
    def test_post2(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info3)
        request.user = self.user
        response = post(request)
        
        self.assertFalse(Product.objects.filter(name = "db negative price", price = -100).exists())

    def test_post3(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info3)
        request.user = self.user
        response = post(request)
        
        self.assertFalse(Product.objects.filter(name = "db2", price = -10).exists())


    def test_post4(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info4)
        request.user = self.user
        response = post(request)
        
        self.assertFalse(Product.objects.filter(name = "db3", price = 10).exists())
        
    def test_post5(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info5)
        request.user = self.user
        response = post(request)
        
        self.assertTrue(Product.objects.filter(name = "db3", price = 10).exists())   
        
    def test_post6(self):
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        request = self.factory.post('/polls/post/', data = self.product_info6)
        request.user = self.user
        response = post(request)
        
        self.assertFalse(Product.objects.filter(name = "egeorgeorgjeorgjeogjeorgjerogjeoigjeogjoejfo2jro23rongoengoengoerjgeogjeogjeogjeogjeogjeogjeogeogjeogjeogjeogjeojgoejgoejgoerjerogjerogjeogjeo", price = 100).exists())     
        
    def test_delete1(self):
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
        
    def test_delete2(self):
        request = self.factory.post('/polls/post/', data = self.product_info7)
        request.user = self.user
        post(request)
        
        q = Product.objects.get(name = "abc", price = 200)
        self.assertTrue(Product.objects.filter(name = "abc").exists())
        self.assertEqual(q.description, "text book for the abc")
        
        request = self.factory.post("/polls/delete/", {'delete': "abc"})
        request.user = self.user
        delete(request)
        
        self.assertFalse(Product.objects.filter(name = "abc").exists())    
