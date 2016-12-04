''' module model to interface db and controller '''
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    ''' Product class for all products '''
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    def addProduct(self):
        ''' add Product to db'''
        if (float)(self.price) < 0 or (float)(self.price) > 1000000:
            return None
        if len(self.name) > 30 or len(self.description) > 30:
            return None
        if self.category not in ["books", "furniture", "others"]:
            return None
        self.save()

    @staticmethod
    def deleteProduct(name, username):
        ''' delete Product from db'''
        try:
            product = Product.objects.get(name=name, username=username)
        except:
            product = None
        if product:
            product.delete()

    @staticmethod
    def updateProduct(name, username, my_price, my_description):
        ''' update Product from db'''
        if (float)(my_price) < 0 or (float)(my_price) > 1000000:
            return None
        if len(my_description) > 30:
            return None
        try:
            product = Product.objects.get(name=name, username=username)
        except:
            product = None
        if product:
            product.price = my_price
            product.description = my_description
            product.save()

    @staticmethod
    def checkDuplicateProduct(name, username):
        ''' check duplicate to ensure unique product name'''
        for obj in Product.objects.all():
            p_name = obj.name
            u_name = obj.username
            if name == p_name and username == u_name:
                return True
        return False

    def __str__(self):
        return self.name


class Image(models.Model):
    ''' Image upload '''
    name = models.CharField(max_length=30)
    pic = models.ImageField()

    def addImage(self):
        ''' add image to db '''
        self.save()

    def getUrl(self):
        ''' get image url'''
        return self.pic.url
