from django.test import TestCase
from polls.models import Product

class ProductTestCase(TestCase):
    def create_product(self, name, price, description, category):
        p=Product()        
        p.name = name
        p.price =price
        p.category= category
        p.description = description
        return p

    def test_whatever_creation1_failrange(self):
        w = self.create_product(name = "1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", price = 100, description="test_name", category="books")
        p=w.addProduct()
        self.assertFalse(Product.objects.filter(name = "1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", price =100).exists())
        self.assertEqual(p, None)
        
    def test_whatever_creation2_failrange(self):
        w = self.create_product(name = "test_desciption", price = 200, category = "books", description="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        p= w.addProduct()
        self.assertEqual(p, None)

    def test_whatever_creation3_failrange(self):
        w = self.create_product(name = "test_category", price = 200, category = "shoes", description="test")
        p = w.addProduct()
        self.assertEqual(p, None)