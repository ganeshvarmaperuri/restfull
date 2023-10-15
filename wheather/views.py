from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Weather, Temperature
from .serializers import WeatherSerializer, TemperatureSerializer


# class WeatherDataListCreateView(generics.ListCreateAPIView):
#     # queryset = Weather.objects.all()
#     serializer_class = WeatherSerializer
#
#     def get_queryset(self):
#         if self.request.method == 'GET':
#             queryset = Weather.objects.all()
#             if 'id' in self.request.query_params:
#                 queryset = queryset.get(id=self.request.query_params['id'])
#             return queryset
#
#     def create(self, request, *args, **kwargs):
#         data = request.data
#         serializer = self.get_serializer(data=data)
#
#         if serializer.is_valid():
#             # Save the WeatherData instance
#             weather_data_instance = serializer.save()
#
#             # Create Temperature instances and associate them with WeatherData
#             temperature_values = data.get('temperature', [])
#             for temp_value in temperature_values:
#                 Temperature.objects.create(weather=weather_data_instance, temperature=temp_value)
#
#             return Response(serializer.data, status=201)
#
#         return Response(serializer.errors, status=400)


class WeatherDataListCreateView(APIView):
    def get(self, request, format=None):
        queryset = Weather.objects.all()
        if "id" in self.request.query_params:
            queryset = queryset.get(id=self.request.query_params["id"])
            serializer = WeatherSerializer(queryset)
        else:
            serializer = WeatherSerializer(queryset, many=True)

        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            weather_report = serializer.save()
            temperature = request.data.get("temperature", None)
            if temperature:
                for temp in temperature:
                    Temperature.objects.create(weather=weather_report, temperature=temp)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
