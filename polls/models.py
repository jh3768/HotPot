''' module model to interface db and controller '''
from __future__ import unicode_literals
from django.db import models
from django import forms

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

    def deleteProduct(self):
        ''' delete Product from db'''
        self.delete()

    def updateProduct(self, my_price, my_description):
        ''' update Product from db'''
        if (float)(my_price) < 0 or (float)(my_price) > 1000000:
            return None
        if len(my_description) > 30:
            return None
        self.price = my_price
        self.description = my_description
        self.save()

    def checkDuplicateProduct(name):
        for obj in Product.objects.all():
            p_name = obj.name
            if name == p_name:
                return True
        return False

    def __str__(self):
        return self.name


class ImageForm(forms.Form):
    """ Image upload form."""
    name = forms.CharField(max_length=100)
    image = forms.ImageField()


class Image(models.Model):
    ''' Image upload '''
    name = models.CharField(max_length=30)
    pic = models.ImageField()

    def addImage(self):
        ''' add image to db '''
        self.save()
