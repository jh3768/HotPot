from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):    
    def test_whatever_creation1(self):
        p=Product()
        p.name = "only a test1"
        p.price = 100
        p.addProduct()
        self.assertTrue(isinstance(p, Product))

    def tearDown(self):
        Product.objects.get(name="only a test1").delete()

    