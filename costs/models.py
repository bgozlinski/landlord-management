from django.db import models
from flats.models import Flat


class Cost(models.Model):
    COST_TYPE_CHOICES = (
        ('electricity', 'Electricity'),
        ('gas', 'Gas'),
        ('water', 'Water'),
        ('other', 'Other'),
    )
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='costs')
    cost_type = models.CharField(max_length=20, choices=COST_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    cost_date_to_pay = models.DateField()
    cost_is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.flat} {self.amount} {self.invoice_number} {self.invoice_date} {self.cost_date_to_pay} {self.cost_is_paid}'

