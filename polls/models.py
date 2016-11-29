from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils import timezone
import datetime

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=200)

    ''' add Product to db'''
    def addProduct(self):
        if ((float)(self.price) < 0 or (float)(self.price) > 1000000):
            return None
        if (len(self.name) > 30 or len(self.description) > 30):
            return None
        self.save()


    def deleteProduct(myName, user_name):
        try:
            p = Product.objects.get(name=myName, username = user_name)
        except Product.DoesNotExist:
            p = None
        if p:
            p.delete()
        else: 
            msg = "does not exists"
            print (msg)


    def updateProduct(myName, myPrice, myDescription ):
        try:
            p = Product.objects.get(name=myName)
        except Product.DoesNotExist:
            p= None
        if p:
            p.price = myPrice
            p.description = myDescription
            p.save()
        else: 
            msg = "does not exists"
            print (msg)

          

    def __str__(self):
        return self.name
    
    
class ImageForm(forms.Form):
    """Image upload form."""
    name = forms.CharField(max_length = 100)
    image = forms.ImageField()
        
    
class Image(models.Model):
    #path = models.CharField(max_length = 300)
    name = models.CharField(max_length = 30)
    pic = models.ImageField(upload_to = 'Users/img/%Y/%m/%d')

    def addImage(self): 
        self.save()
    
#     class Meta:
#         db_table = "image"
#      

        


