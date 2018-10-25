from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField()
    price
    category



class Market(models.Model):
    pass

