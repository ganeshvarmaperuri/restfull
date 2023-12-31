# Generated by Django 4.2.5 on 2023-09-19 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Weather",
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
                ("date", models.DateField()),
                ("lat", models.DecimalField(decimal_places=6, max_digits=8)),
                ("lot", models.DecimalField(decimal_places=6, max_digits=8)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Temperature",
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
                ("temperature", models.FloatField()),
                (
                    "weather",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wheather.weather",
                    ),
                ),
            ],
        ),
    ]
