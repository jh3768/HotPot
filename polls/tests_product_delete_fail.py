from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Introduction to computer system", price=100, description= "user1", username = "user1")
        Product.objects.create(name="Introduction to database", price=200, description= "user2",username = "user2")
        Product.objects.create(name="Introduction to algorithms", price=300, description= "user3", username = "user3")
        Product.objects.create(name="Introduction to computer science", price=400, description= "user4", username = "user4")
        Product.objects.create(name="Introduction to operating system", price=500, description= "user5", username = "user5")
        Product.objects.create(name="Introduction to computer network", price=600, description= "user6",username = "user6")
        Product.objects.create(name="Introduction to UI design", price=700, description= "user7", username = "user7")
        Product.objects.create(name="Introduction to machine learning", price=800, description= "user8", username = "user8")
        Product.objects.create(name="Introduction to software engineering", price=900, description= "user9", username = "user9")
        Product.objects.create(name="Introduction to data science", price=1000, description= "user10", username = "user10")
        

    def test_delete_product_fail1 (self):
        p=Product()
        p.name = "Introduction to computer system 1"
        p.username = "user 1"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")


    def test_delete_product_fail2 (self):
        p=Product()
        p.name = "Introduction to database 1"
        p.username = "user 2"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")

    def test_delete_product_fail3 (self):
        p=Product()
        p.name = "Introduction to data science 1"
        p.username = "user 3"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")


    def test_delete_product_fail4 (self):
        p=Product()
        p.name = "Introduction to software engineering 1"
        p.username = "user 4"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")

    def test_delete_product_fail5 (self):
        p=Product()
        p.name = "Introduction to algorithms 1"
        p.username = "user 5"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")

    def test_delete_product_fail6 (self):
        p=Product()
        p.name = "Introduction to computer network 1"
        p.username = "user 6"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")

    def test_delete_product_fail7 (self):
        p=Product()
        p.name = "Introduction to computer system 1"
        p.username = "user 7"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")

    def test_delete_product_fail8 (self):
        p=Product()
        p.name = "Introduction to statistics 1"
        p.username = "user 8"
        self.assertFalse(Product.objects.filter(name = p.name).exists())
        p= Product.deleteProduct(p.name, p.username)
        self.assertEqual(p, "object does not exist")



   
