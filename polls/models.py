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
    def __str__(self):
        return self.name

    def post(self):
        
