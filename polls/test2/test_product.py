from django.test import TestCase
from polls.models import Product

class SimpleTest(TestCase):
    def test_add_product(self):
        p = Product()
        p.name = "test_product"
        p.price = 100
        p.description = "test1"
        p.category= "books"
        p.username = "user1"  
        p.url = "static/media/index.png"  
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product").exists())

    def test_str_product(self):
        p = Product()
        p.name = "test_product"
        p.price = 100
        p.description = "test1"
        p.category= "books"
        p.username = "user1"  
        p.url = "static/media/index.png"  
        p.addProduct()
        self.assertEqual(p.__str__(), p.name)
   
    def teardown(self):
        Product.objects.filter(name = 'test_product').delete()
       






