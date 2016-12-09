from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    
    def create_product(self, name, price):
        p=Product()        
        p.name = name
        p.price =price
        p.category ="books"
        return p

    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "only a test1", price = -100)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test1").exists())

    def test_whatever_creation2_failrange(self):
        w = self.create_product(name = "only a test2", price = -100000000000000000000)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test2").exists())

    def test_whatever_creation3_failrange(self):
        w = self.create_product(name = "only a test3", price = -100088888888888888888800000000000000000)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test3").exists())


    def test_whatever_creation4_failrange(self):
        w = self.create_product(name = "only a test4", price = -0.000001)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test4").exists())


    def test_whatever_creation5_failrange(self):
        w = self.create_product(name = "only a test5", price = -1 )
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test5").exists())

    def test_whatever_creation6_failrange(self):
        w = self.create_product(name = "only a test6", price = -0.000000000000000001 )
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test6").exists())

    def test_whatever_creation7_failrange(self):
        w = self.create_product(name = "only a test7", price = -0.0000000000000000000000000000000000003434324234324324234 )
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test7").exists())

    def test_whatever_creation8_failrange(self):
        w = self.create_product(name = "only a test8", price = -3.434324234324324234 )
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test8").exists())



    def test_whatever_creation9_failrange(self):
        w = self.create_product(name = "only a test9", price = -3434324234324324234 )
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test9").exists())

    def test_whatever_creation10_failrange(self):
        w = self.create_product(name = "only a test10", price = -3434324234324324234888888888888888888888888888888888888888888888888)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test10").exists())

    
    def test_whatever_creation11_failrange(self):
        w = self.create_product(name = "only a test11", price = 3434324234324324234888888888888888888888888888888888888888888888888)
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "only a test11").exists())