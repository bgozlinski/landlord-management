from django.db import models
from flats.models import Flat
from tenants.models import Tenant


class Rent(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='rents')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='rents')
    amount_total = models.DecimalField(max_digits=10, decimal_places=2)
    rent_begin = models.DateField(blank=True, null=True)
    rent_stop = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.flat} {self.tenant}'
