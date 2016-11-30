from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="which class is the most difficult", price=100, description= "user1")
        Product.objects.create(name="Introduction to database", price=200, description= "user2")
        Product.objects.create(name="Introduction to algorithms", price=300, description= "user3")
        Product.objects.create(name="Introduction to computer science", price=400, description= "user4")
        Product.objects.create(name="Introduction to operating system", price=500, description= "user5")
        Product.objects.create(name="Introduction to computer network", price=600, description= "user6")
        Product.objects.create(name="Introduction to UI design", price=700, description= "user7")
        Product.objects.create(name="Introduction to machine learning", price=800, description= "user8")
        Product.objects.create(name="Introduction to software engineering", price=900, description= "user9")
        Product.objects.create(name="Introduction to data science", price=1000, description= "user10")
	    
    def test_product_name1(self):
     
        q = Product.objects.get(name= "which class is the most difficult", price =100)
	
        self.assertEqual(q.name,  "which class is the most difficult")

        self.assertEqual(q.price,  100)
        self.assertEqual(q.description, "user1")


    def test_product_name2(self):
     
        q = Product.objects.get(name= "Introduction to database", price = 200)
    
        self.assertEqual(q.name,  "Introduction to database")

        self.assertEqual(q.price,  200)
        self.assertEqual(q.description, "user2")

    def test_product_name3(self):
     
        q = Product.objects.get(name= "Introduction to algorithms", price = 300)
    
        self.assertEqual(q.name,  "Introduction to algorithms")

        self.assertEqual(q.price,  300)
        self.assertEqual(q.description, "user3")


    def test_product_name4(self):
     
        q = Product.objects.get(name= "Introduction to computer science", price = 400)
    
        self.assertEqual(q.name,  "Introduction to computer science")

        self.assertEqual(q.price,  400)
        self.assertEqual(q.description, "user4")


    def test_product_name5(self):
        q = Product.objects.get(name= "Introduction to operating system", price = 500)
    
        self.assertEqual(q.name,  "Introduction to operating system")

        self.assertEqual(q.price,  500)
        self.assertEqual(q.description, "user5")

    def test_product_name6(self):
        q = Product.objects.get(name= "Introduction to computer network", price = 600)
    
        self.assertEqual(q.name,  "Introduction to computer network")

        self.assertEqual(q.price,  600)
        self.assertEqual(q.description, "user6")

    def test_product_name7(self): 
        q = Product.objects.get(name= "Introduction to UI design", price = 700)
    
        self.assertEqual(q.name,  "Introduction to UI design")

        self.assertEqual(q.price,  700)
        self.assertEqual(q.description, "user7")

    def test_product_name8(self): 
        q = Product.objects.get(name= "Introduction to machine learning", price = 800)
    
        self.assertEqual(q.name,  "Introduction to machine learning")

        self.assertEqual(q.price,  800)
        self.assertEqual(q.description, "user8")

    def test_product_name9(self): 
        q = Product.objects.get(name= "Introduction to software engineering", price = 900)
    
        self.assertEqual(q.name,  "Introduction to software engineering")

        self.assertEqual(q.price,  900)
        self.assertEqual(q.description, "user9")

    def test_product_name9(self): 
        q = Product.objects.get(name= "Introduction to data science", price = 1000)
    
        self.assertEqual(q.name,  "Introduction to data science")

        self.assertEqual(q.price,  1000)
        self.assertEqual(q.description, "user10")

