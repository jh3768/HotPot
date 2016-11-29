from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="only a test", price=100, description= "user1")

    def test_whatever_creation1(self):
        p=Product()
        p.name = "only a test1"
        p.price = 100
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation2(self):
        p=Product()
        p.name = "only a test2"
        p.price = 200
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation3(self):
        p=Product()
        p.name = "only a test3"
        p.price = 300
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation4(self):
        p=Product()
        p.name = "only a test4"
        p.price = 400
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation5(self):
        p=Product()
        p.name = "only a test5"
        p.price = 500
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation6(self):
        p=Product()
        p.name = "only a test6"
        p.price = 600
        p.addProduct()
        self.assertTrue(isinstance(p, Product))


    def test_whatever_creation7(self):
        p=Product()
        p.name = "only a test7"
        p.price = 700
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation8(self):
        p=Product()
        p.name = "only a test8"
        p.price = 800
        p.addProduct()
        self.assertTrue(isinstance(p, Product)) 
    
    def test_whatever_creation9(self):
        p=Product()
        p.name = "only a test9"
        p.price = 900
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def test_whatever_creation10(self):
        p=Product()
        p.name = "only a test10"
        p.price = 1000
        p.addProduct()
        self.assertTrue(isinstance(p, Product))
        
