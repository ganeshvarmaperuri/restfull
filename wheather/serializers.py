from rest_framework import serializers
from .models import Weather, Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ["temperature"]


class WeatherSerializer(serializers.ModelSerializer):
    temperature = serializers.SerializerMethodField()

    class Meta:
        model = Weather
        fields = ["id", "date", "lat", "lot", "city", "state", "temperature"]

    def get_temperature(self, obj):
        # Get the related temperature objects for the WeatherData instance
        temperature_objects = obj.temperature.all()

        # Extract and return a list of temperature values
        temperature_values = [temp.temperature for temp in temperature_objects]
        return temperature_values
