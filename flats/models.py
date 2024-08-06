from django.db import models


class Flat(models.Model):
    city_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10)
    flat_floor = models.IntegerField()
    flat_size_sqm = models.FloatField()

    def __str__(self):
        return f'{self.city_name} {self.street_name} {self.street_number}/{self.flat_number} '
