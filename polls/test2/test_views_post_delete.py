from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from polls.views import post, delete
from polls.models import Product, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import RequestFactory
from django.core.files import File
import os
from polls.forms import UploadFileForm
from django.urls import reverse

class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('temporary2@gmail.com', 'temporary2@gmail.com', 'temporary2')
        self.c = Client()
        self.c.login(username='temporary2@gmail.com', password='temporary2')
        self.factory = RequestFactory()
        self.product_info1 = {'name': "Intro to algorithm", 'price':200, 'description' : "text book for the algorithms", 'username': 'temporary2@gmail.com', 'category': "books"}
        self.product_info2 = {'name': "db", 'price':100, 'description' : "text book for the db", 'username': 'temporary2@gmail.com', 'category': "books"}
        self.img2 = Image()
        self.img2.name = "test_image222"
        self.img2.pic = SimpleUploadedFile(name=self.img2.name, content=open("polls/test2/test_image.png", 'rb').read(), content_type='image/png')
    
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
        request = self.factory.post('/polls/post/', data = self.product_info1)
        request.user = self.user
        response = post(request)
        
        query = Product.objects.get(name = "Intro to algorithm", price = 200)
        
        self.assertEqual(query.description, "text book for the algorithms")
        self.assertEqual(query.name, "Intro to algorithm")
        self.assertEqual(query.price, 200)
        response = post(request)
        self.assertEqual(response.status_code, 302)



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
        
    def test_edit(self):
        request = self.factory.post('/polls/post/', data = self.product_info2)
        request.user = self.user
        post(request)
        
        q = Product.objects.get(name = "db", price = 100)
        self.assertTrue(Product.objects.filter(name = "db").exists())
        self.assertEqual(q.description, "text book for the db")
        
        request = self.factory.post("/polls/edit/", {'name': 'db', 'price':200, 'description' : "text book for the db", 'username': 'temporary2@gmail.com', 'category': "books"})
        request.user = self.user
        delete(request)
        query = Product.objects.get(name = "db")
        
        self.assertEqual(query.price, 200)

    def test_addImage3(self):
        pic= SimpleUploadedFile(name=self.img2.name, content=open("polls/test2/test_image.png", 'rb').read(), content_type='image/png')
        request = self.factory.post('/polls/post/', {'name': 'db test', 'price':200, 'description' : "text book for the db", 'username': "temporary2@gmail.com", 'category': "books", 'pic': pic})
        MyImageForm = UploadFileForm(request.POST, request.FILES)
        self.assertTrue(MyImageForm.is_valid())



    def test_post3(self):
        pic= SimpleUploadedFile(name=self.img2.name, content=open("polls/test2/test_image.png", 'rb').read(), content_type='image/png')
        request = self.factory.post('/polls/post/', {'name': 'db test2', 'price':200, 'description' : "text book for the db", 'username': "temporary2@gmail.com", 'category': "books", 'pic': pic})
        request.user = self.user
        response = post(request)
        query = Product.objects.get(name = "db test2", price = 200)
        self.assertEqual(query.name, "db test2")
        self.assertEqual(query.price, 200)
        self.assertEqual(response.status_code, 302)

    def teardown(self):
        Product.objects.filter(name = "Intro to algorithm").delete()
        Product.objects.filter(name = "db test").delete()
        Product.objects.filter(name = "db test2").delete()
    
   