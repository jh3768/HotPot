from __future__ import unicode_literals

from django.db import models
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
    	p = Product.objects.get(name=myName, username = user_name)
    	p.delete()

    def __str__(self):
        return self.name


