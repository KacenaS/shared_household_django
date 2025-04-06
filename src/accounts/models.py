from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add custom fields if you want
    is_house_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=30, blank=True)