from django.db import models


class Topping(models.Model):
    topping_name = models.CharField(max_length=50)
    price = models.FloatField()


class Pizza(models.Model):
    topping_list = models.ManyToManyField(Topping)
    price = models.FloatField()
