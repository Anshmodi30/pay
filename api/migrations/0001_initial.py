# Generated by Django 4.2.5 on 2024-02-22 17:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LoanAmout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fname", models.CharField(default="", max_length=30)),
                ("lname", models.CharField(default="", max_length=30)),
                ("appartment", models.CharField(default="", max_length=100)),
                ("postalCode", models.CharField(default="", max_length=6)),
                ("city", models.CharField(default="", max_length=30)),
                ("email", models.EmailField(max_length=30)),
                (
                    "alternate",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("sin", models.CharField(max_length=6)),
                ("title", models.CharField(default="", max_length=30)),
                ("month", models.IntegerField()),
                ("day", models.IntegerField()),
                ("year", models.IntegerField()),
                ("martialStatus", models.CharField(default="", max_length=10)),
                ("amount", models.IntegerField()),
                ("address", models.TextField(blank=True)),
            ],
        ),
    ]