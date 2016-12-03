from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def create_product(self, name, price, desciption, category):
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

   

    
