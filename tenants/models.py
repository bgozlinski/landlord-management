from django.db import models
from flats.models import Flat


class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='tenants')



