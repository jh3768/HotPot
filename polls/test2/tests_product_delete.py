from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Introduction to computer system test", price=100, description="user1", username="123@123", category="books")
        
    def test_delete_product (self):
        p = Product.objects.get(name= "Introduction to computer system test")    
        self.assertTrue(isinstance(p, Product))
        p.deleteProduct(name="Introduction to computer system test", username="123@123")
        self.assertFalse(Product.objects.filter(name = "Introduction to computer system test").exists())
