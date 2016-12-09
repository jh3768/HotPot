from django.test import TestCase

from polls.models import Product



class SimpleTest(TestCase):
    def setUp(self):
        p = Product()
        p.name = "test_product_fail"
        p.username = "123@123"
        p.price = 100
        p.description = "user_fail"
        p.category= "books"    
        p.addProduct()

    def test_update_product_fail1(self):
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p = Product.objects.get(name="test_product_fail")
        p = Product.updateProduct(name="test_product_fail", username="123@123", my_price=-200, my_description="user_fail1")
        self.assertEqual(p, None)
    

    def test_update_product_fail12(self):
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p = Product.objects.get(name="test_product_fail")
        p = Product.updateProduct(name="test_product_fail", username="123@123", my_price=-0.0000001, my_description="user_fail2")
        self.assertEqual(p, None)


    def test_update_product_fail13(self):
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p = Product.objects.get(name="test_product_fail")
        p= Product.updateProduct(name="test_product_fail", username="123@123", my_price=100000000000, my_description="user_fail3")
        self.assertEqual(p, None)

    def test_update_product_fail14(self):
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p = Product.objects.get(name="test_product_fail")
        p = Product.updateProduct(name="test_product_fail", username="123@123", my_price=100, my_description="user_fail3*8*************************************************************")
        self.assertEqual(p, None)

    def test_update_product_fail15(self):
        self.assertTrue(Product.objects.filter(name="test_product_fail").exists())
        p = Product.objects.get(name="test_product_fail")
        p = Product.updateProduct(name="test_product_fail*", username="123@123", my_price=100, my_description="user_fail")
        self.assertEqual(p, None)

    def tearDown(self):
        Product.objects.get(name="test_product_fail").delete()