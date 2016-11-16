from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Introduction to computer system", price=100, description= "user1")
        Product.objects.create(name="Introduction to database", price=200, description= "user2")
        Product.objects.create(name="Introduction to algorithms", price=300, description= "user3")
        Product.objects.create(name="Introduction to computer science", price=400, description= "user4")
        Product.objects.create(name="Introduction to operating system", price=500, description= "user5")
        Product.objects.create(name="Introduction to computer network", price=600, description= "user6")
        Product.objects.create(name="Introduction to UI design", price=700, description= "user7")
        Product.objects.create(name="Introduction to machine learning", price=800, description= "user8")
        Product.objects.create(name="Introduction to software engineering", price=900, description= "user9")
        Product.objects.create(name="Introduction to data science", price=1000, description= "user10")
        

    def test_delete_product1_fail (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to computer system 1").exists())
        a = Product.objects.filter(name = "Introduction to computer system 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))

    def test_delete_product2_fail (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to database 1").exists())
        a = Product.objects.filter(name = "Introduction to database 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))

    def test_delete_product3_fail (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to algorithms 1").exists())
        a = Product.objects.filter(name = "Introduction to algorithms 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))


    def test_delete_product4_fail (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to computer science 1").exists())
        a = Product.objects.filter(name = "Introduction to computer science 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))

    def test_delete_product5 (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to operating system 1").exists())
        a = Product.objects.filter(name = "Introduction to operating system 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))

    def test_delete_product6 (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to computer network 1").exists())
        a = Product.objects.filter(name = "Introduction to computer network 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))

    def test_delete_product7 (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to UI design 1").exists())
        a = Product.objects.filter(name = "Introduction to UI design 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))
        

    def test_delete_product8 (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to machine learning 1").exists())
        a = Product.objects.filter(name = "Introduction to machine learning 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))

    def test_delete_product9 (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to software engineering 1").exists())
        a = Product.objects.filter(name = "Introduction to software engineering 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))


    def test_delete_product9 (self):
        self.assertFalse(Product.objects.filter(name = "Introduction to data science 1").exists())
        a = Product.objects.filter(name = "Introduction to data science 1").delete()
        self.assertEqual (a, (0, {"polls.Product":0}))
   


    
