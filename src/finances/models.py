from django.db import models
from django.contrib.auth.models import User
from households.models import Household
from shared_household import settings


class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.amount} by {self.paid_by}"