from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
   
    def test_delete_product_fail (self):
        p=Product()
        p.name = "Introduction to computer system 1"
        p.username = "user 1"
        p.category="books"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p.deleteProduct(p.name, p.username)
     






   
