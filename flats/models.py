from django.db import models


class Flat(models.Model):
    city_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=255)
    street_number = models.CharField()
    flat_number = models.CharField()
    flat_floor = models.IntegerField()
    flat_size_sqm = models.FloatField()