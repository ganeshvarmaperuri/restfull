from django.db import models


class Weather(models.Model):
    date = models.DateField()
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lot = models.DecimalField(max_digits=8, decimal_places=6)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class Temperature(models.Model):
    weather = models.ForeignKey(
        Weather, on_delete=models.CASCADE, related_name="temperature"
    )
    temperature = models.FloatField()
