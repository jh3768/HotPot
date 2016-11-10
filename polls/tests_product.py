from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="which class is the most difficult", price=100, description= "yanan")
	
        
    def test_product_name(self):
     
        q = Product.objects.get(name= "which class is the most difficult", price =100)
	
        self.assertEqual(q.name,  "which class is the most difficult")

        self.assertEqual(q.price,  100)
        self.assertEqual(q.description, "yanan")


    def create_question(self, name="only a test", price =100):
        return Product.objects.create(name= name, price=price)

    def test_whatever_creation(self):
        w = self.create_question()
        self.assertTrue(isinstance(w, Product))

    def test_delete_question (self):
        w = self.create_question()
        Product.objects.filter(name = w.name).delete()
        
        self.assertFalse(Product.objects.filter(name = "only a test").exists())
