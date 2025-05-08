from django.contrib.auth.models import User
from django.db import models

from shared_household import settings


class Household(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'household')