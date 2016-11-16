from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="only a test1", price=100, description= "user1")
	

    def create_product(self, name="only a test1", price =100):
        return Product.objects.create(name= name, price=price)

    def test_whatever_creation1_failnegative(self):
        w = self.create_product(name = "only a test1", price = -99999999999999)
        self.assertFalse(isinstance(w, Product))

    def test_whatever_creation2_failnegative(self):
        w = self.create_product(name = "only a test2", price = -100)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation3_fialnegative(self):
        w = self.create_product(name = "only a test3", price = -400)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation4_failnegative(self):
        w = self.create_product(name = "only a test4", price = -888888888888888888888)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation5_failnegative(self):
        w = self.create_product(name = "only a test5", price = -12000000000000000000000000)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation6_failnegative(self):
        w = self.create_product(name = "only a test6", price = -0.01)
        self.assertTrue(isinstance(w, Product))


    def test_whatever_creation7_failnegative(self):
        w = self.create_product(name = "only a test7", price = -1)
        self.assertTrue(isinstance(w, Product))


    def test_whatever_creation8_failnegative(self):
        w = self.create_product(name = "only a test8", price = -0.0000000000000000001)
        self.assertTrue(isinstance(w, Product)) 
    
    def test_whatever_creation9_failnegative(self):
        w = self.create_product(name = "only a test9", price = -500)


    def test_whatever_creation10_failnegative(self):
        w = self.create_product(name = "only a test10", price = -800000000000000000)
        self.assertTrue(isinstance(w, Product))
        
