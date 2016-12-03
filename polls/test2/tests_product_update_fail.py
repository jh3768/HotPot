from django.test import TestCase

from polls.models import Product



class SimpleTest(TestCase):
    def test_update_product_fail1(self):
        p = Product()
        p.name = "test_product_fail"
        p.price = 100
        p.description = "user_fail"
        p.category= "books"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p.updateProduct(my_price =-200, my_description= "user_fail1")
        self.assertEqual(p.price, 100)
        self.assertEqual(p.description, "user_fail")

    def test_update_product_fail12(self):
        p = Product()
        p.name = "test_product_fail"
        p.price = 100
        p.description = "user_fail"
        p.category= "books"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p.updateProduct(my_price =-0.0000001, my_description= "user_fail2")
        self.assertEqual(p.price, 100)
        self.assertEqual(p.description, "user_fail")


    def test_update_product_fail13(self):
        p = Product()
        p.name = "test_product_fail"
        p.price = 100
        p.description = "user_fail"
        p.category= "books"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p.updateProduct(my_price = 10000000, my_description= "user_fail3")
        self.assertEqual(p.price, 100)
        self.assertEqual(p.description, "user_fail")

    def test_update_product_fail14(self):
        p = Product()
        p.name = "test_product_fail"
        p.price = 100
        p.description = "user_fail"
        p.category= "books"    
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p.updateProduct(my_price= 100, my_description= "user_fail3*8*************************************************************")
        self.assertEqual(p.price, 100)
        self.assertEqual(p.description, "user_fail")

    def tearDown(self):
        Product.objects.get(name="test_product_fail").delete()