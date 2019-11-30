from rest_framework import serializers
from .models import FlightModel

class FlightModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = FlightModel
    fields = '__all__'