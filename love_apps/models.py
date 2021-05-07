from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    availabilty = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to = "images/product")

class TopPicks(models.Model):
    class Meta:
        verbose_name = "TopPicks"
        verbose_name_plural = "Top Picks"
    name = models.CharField(max_length=200)
    description = models.TextField()
    availabilty = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to = "images/toppicks")

class BestSeller(models.Model):
    class Meta:
        verbose_name = "BestSellers"
        verbose_name_plural = "Best Sellers"
    name = models.CharField(max_length=200)
    description = models.TextField()
    availabilty = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to = "images/bestseller")

class NewArrivals(models.Model):
    class Meta:
        verbose_name = "NewArrivals"
        verbose_name_plural = "New Arrivals"
    name = models.CharField(max_length=200)
    description = models.TextField()
    availabilty = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to = "images/newarrivals")

class ComingSoon(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    availabilty = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to = "images/coming")