from django.test import TestCase

from polls.models import Product



class SimpleTest(TestCase):

    def test_update_product(self):
        p = Product()
        p.name = "test_product2"
        p.username = "123@123"
        p.price = 100
        p.description = "user2"
        p.category= "books"    
        p.addProduct()   
        self.assertTrue(Product.objects.filter(name="test_product2").exists()) 
        Product.updateProduct(name="test_product2", username="123@123", my_price=200, my_description= "user3")
        p =  Product.objects.get(name="test_product2") 
        self.assertEqual(p.price, 200)
        self.assertEqual(p.description, "user3")

    def tearDown(self):
        Product.objects.get(name="test_product2").delete()