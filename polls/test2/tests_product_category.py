from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="computer system", price=10, description= "user")
    

    def create_product(self, name="computer system", price =100, desciption = "user", category ="book"):
        p=Product()        
        p.name = name
        p.price =price
        p.desciption = desciption
        p.category= category
        return p

    def test_category_fail(self):
        w = self.create_product(name = "computer system", price = 100, desciption= "nothing", category="shoes")
        w.addProduct()
        self.assertFalse(Product.objects.filter(name = "computer system").exists())

   

    
