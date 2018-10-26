from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICE = (
        ('electronics', 'electronics'),
        ('beverages', 'beverages'),
        ('cleaners', 'cleaners'),
        ('clothing', 'clothing'),
        ('baking goods', 'baking goods'),
        ('frozen foods', 'frozen foods'),
        ('fresh foods', 'fresh foods'),
        ('paper goods', 'paper goods'),
        ('other','other'),
    )
    name = models.CharField(max_length=70)
    price = models.PositiveIntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=20)
    picture = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def search_bar(cls,search_term):
        return cls.objects.filter(name__icontains=search_term)


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.PositiveSmallIntegerField(default=0)


@receiver(post_save, sender=Product)
def update_stock(sender, instance, created, **kwargs):
    if created:
        Stock.objects.create(product=instance)
    instance.stock.save()


@receiver(post_save, sender=Product)
def save_stock(sender, instance, **kwargs):
    instance.stock.save()
