from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    postcode = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=24)
    gis = models.CharField(max_length=64)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    rating_counter = models.IntegerField(default=0)
    delivery_time = models.CharField(max_length=64, null=True)
    delivery_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    minimum_order_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    free_delivery = models.DecimalField(max_digits=6, decimal_places=2, null=True)


class Section(models.Model):
    name = models.CharField(max_length=64)
    restaurants = models.ManyToManyField(Restaurant)
    description = models.CharField(max_length=1000)


class Food(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sections = models.ManyToManyField(Section)


class Kind(models.Model):
    name = models.CharField(max_length=64)
    restaurants = models.ManyToManyField(Restaurant, related_name='kind_list')
