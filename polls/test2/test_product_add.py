from django.test import TestCase
from polls.models import Product

class SimpleTest(TestCase):
    def test_add_product(self):
        p = Product()
        p.name = "test_product"
        p.price = 100
        p.description = "user1"
        p.category= "books"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product").exists())

    def test_add_product2(self):
        p = Product()
        p.name = "test_others"
        p.price = 100
        p.description = "user1"
        p.category= "others"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_others").exists())
    
    def teardown(self):
        Product.objects.filter(name= "test_product").delete()
        Product.objects.filter(name= "test_others").delete()



