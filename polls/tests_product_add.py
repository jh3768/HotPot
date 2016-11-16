from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="only a test1", price=100, description= "user1")
	

    def create_product(self, name="only a test1", price =100):
        return Product.objects.create(name= name, price=price)

    def test_whatever_creation1(self):
        w = self.create_product(name = "only a test1", price = 100)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation2(self):
        w = self.create_product(name = "only a test2", price = 200)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation3(self):
        w = self.create_product(name = "only a test3", price = 300)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation4(self):
        w = self.create_product(name = "only a test4", price = 400)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation5(self):
        w = self.create_product(name = "only a test5", price = 500)
        self.assertTrue(isinstance(w, Product))

    def test_whatever_creation6(self):
        w = self.create_product(name = "only a test6", price = 600)
        self.assertTrue(isinstance(w, Product))


    def test_whatever_creation7(self):
        w = self.create_product(name = "only a test7", price = 700)
        self.assertTrue(isinstance(w, Product))


    def test_whatever_creation8(self):
        w = self.create_product(name = "only a test8", price = 800)
        self.assertTrue(isinstance(w, Product)) 
    
    def test_whatever_creation9(self):
        w = self.create_product(name = "only a test9", price = 900)


    def test_whatever_creation10(self):
        w = self.create_product(name = "only a test10", price = 1000)
        self.assertTrue(isinstance(w, Product))
        