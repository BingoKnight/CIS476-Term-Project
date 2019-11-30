from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import StateModelSerializer, CityModelSerializer
from .models import StateModel, CityModel

# @api_view(['GET'])
# def get_states(self):
#   states = StateModel.objects.all()
#   serializer = StateModelSerializer(states, many=True)
#   return HttpResponse(serializer.data)