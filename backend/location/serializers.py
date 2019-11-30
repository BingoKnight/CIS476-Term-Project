from rest_framework import serializers
from .models import StateModel, CityModel

class StateModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = StateModel
    fields = '__all__'

class CityModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityModel
    fields = '__all__'