from django.db import models
from flats.models import Flat
from tenants.models import Tenant


class Rent(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='rents')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='rents')
    amount_total = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
