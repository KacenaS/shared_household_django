# Generated by Django 5.1.7 on 2025-04-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shoppingitem",
            name="category",
            field=models.CharField(
                choices=[
                    ("food", "Food"),
                    ("pharmacy", "Pharmacy"),
                    ("clothes", "Clothes"),
                    ("hardware", "Hardware"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=20,
            ),
        ),
    ]
