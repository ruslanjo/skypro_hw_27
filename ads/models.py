from django.db import models


class Ads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

