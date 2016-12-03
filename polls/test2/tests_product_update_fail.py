from django.test import TestCase

from polls.models import Product



class SimpleTest(TestCase):
    def test_update_product_fail(self):
        p = Product()
        p.name = "test_product_fail"
        p.price = 100
        p.description = "user_fail"
        p.category= "books"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p.updateProduct(my_price =-200, my_description= "user_fail2")
        self.assertTrue(p.price, 100)
        self.assertTrue(p.description, "user_fail2")

    def tearDown(self):
        Product.objects.get(name="test_product_fail").delete()