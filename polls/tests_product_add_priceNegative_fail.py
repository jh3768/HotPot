from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="only a test", price=10, description= "user")
    

    def create_product(self, name="only a test1", price =100):
        p=Product()        
        p.name = name
        p.price =price
        return p

    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "only a test1", price = -100)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test1").exists())

    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "only a test2", price = -100000000000000000000)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test2").exists())

    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "only a test3", price = -100088888888888888888800000000000000000)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test3").exists())


    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "only a test4", price = -0.000001)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test4").exists())


    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "only a test5", price = -1 )
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test5").exists())

    
