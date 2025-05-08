from django.db import models
from django.contrib.auth.models import User
from households.models import Household
from shared_household import settings


class ShoppingItem(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('pharmacy', 'Pharmacy'),
        ('clothes', 'Clothes'),
        ('hardware', 'Hardware'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_urgent = models.BooleanField(default=False)
    is_bought = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + self.category
    
    @classmethod
    def add_item(cls, title, username, household_name):
        from accounts.models import CustomUser
        from households.models import Household

        user = CustomUser.objects.get(username=username)
        household = Household.objects.get(name=household_name)

        return cls.objects.create(
            title=title,
            is_bought=False,
            added_by=user,
            household=household
        )