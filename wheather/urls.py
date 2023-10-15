from django.urls import path, include
from .views import WeatherDataListCreateView

urlpatterns = [path("weather/", WeatherDataListCreateView.as_view(), name="weather")]
