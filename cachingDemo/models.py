from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length = 120)
    price = models.IntegerField()
    