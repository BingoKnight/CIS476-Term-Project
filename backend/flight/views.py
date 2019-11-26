from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from .models import FlightModel
from .serializers import FlightModelSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_data(request):
  data = FlightModel.objects.all()
  serializer = FlightModelSerializer(data, many=True)
  return JsonResponse(serializer.data, safe=False)

