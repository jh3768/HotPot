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

    def tearDown(self):
        Product.objects.get(name="test_product").delete()


