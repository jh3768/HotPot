from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Introduction to computer system test", price=100, description= "user1", username = "user1", category = "books")
        
    def test_delete_product (self):
        p = Product.objects.get(name= "Introduction to computer system test")    
        self.assertTrue(isinstance(p, Product))
        p.deleteProduct()
        self.assertFalse(Product.objects.filter(name = "Introduction to computer system test").exists())

    



   
