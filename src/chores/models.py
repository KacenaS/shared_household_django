from django.db import models
from django.contrib.auth.models import User
from households.models import Household
from shared_household import settings


class Chore(models.Model):
    title = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    is_recurring = models.BooleanField(default=False)
    recurrence_days = models.IntegerField(
        null=True,
        blank=True,
        help_text="Repeat every X days if recurring"
    )

    def __str__(self):
        return f"{self.title} for {self.assigned_to} (due {self.due_date})"