from django.db import models
from django.contrib.auth.models import User
from households.models import Household
from datetime import datetime


class CatFeedingLog(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    fed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Fed by {self.fed_by.username} in {self.household.name} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
