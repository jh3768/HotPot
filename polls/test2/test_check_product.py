from django.test import TestCase
from polls.models import Product

class SimpleTest(TestCase):
    def create_product(self, name, user, price, desciption, category):
        p=Product()        
        p.name = name
        p.username = user
        p.price =price
        p.desciption = desciption
        p.category= category
        return p

    def test_check(self):
        p = self.create_product(name="check duplicate", price=100, desciption="nothing", category="books", user = "user1")
        p.addProduct()
        self.assertTrue(Product.objects.filter(name="check duplicate", username = "user1").exists())
        self.assertEqual(Product.checkDuplicateProduct("check duplicate", "user1"), True)

    def test_check2(self):
        p = self.create_product(name="check duplicate", price=100, desciption="nothing", category="books", user = "user1")
        p.addProduct()
        self.assertFalse(Product.objects.filter(name="check duplicate2", username = "user1").exists())  
        self.assertEqual(Product.checkDuplicateProduct("check duplicate2", "user1"), False)

    def test_check3(self):
        p = self.create_product(name="check duplicate3", price=100, desciption="nothing", category="books", user = "user1")
        p.addProduct() 
        name = p.__str__()
        self.assertEqual(name, "check duplicate3")
       
    def teardown(self):
        Product.objects.filter(name = "check duplicate").delete()
        Product.objects.filter(name = "check duplicate2").delete()
        Product.objects.filter(name = "check duplicate3").delete()
       
