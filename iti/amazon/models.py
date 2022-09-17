from django.db import models


# Create your models here.

# ## represent table in form of class
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=10)
