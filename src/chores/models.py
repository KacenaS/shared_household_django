from django.db import models
from django.contrib.auth.models import User
from households.models import Household
from shared_household import settings


class Chore(models.Model):
    title = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True)
    finished_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='finished_chores'
    )
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    is_recurring = models.BooleanField(default=False)
    recurrence_days = models.IntegerField(
        null=True,
        blank=True,
        help_text="Repeat every X days if recurring"
    )

    def __str__(self):
        return f"{self.title} for {self.assigned_to} (due {self.due_date})"
