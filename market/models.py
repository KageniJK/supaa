from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICE = (
        ('electronics', 'electronics'),
        ('food', 'food'),
        ('soaps', 'soaps'),
        ('clothing', 'clothing'),
    )
    name = models.CharField(max_length=70)
    price = models.PositiveIntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=20)
    picture = models.ImageField(upload_to='products/')
    how_many = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def search_bar(cls,search_term):
        return cls.objects.filter(name__icontains=search_term)


class Market(models.Model):
    pass

