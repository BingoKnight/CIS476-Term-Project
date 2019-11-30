from rest_framework import generics
from rest_framework.response import Response
from .models import StateModel, CityModel
from .serializers import StateModelSerializer, CityModelSerializer

class StateAPI(generics.GenericAPIView):
  serializer_class = StateModelSerializer

# Get all states in the db
  def get(self, *args, **kwargs):
    states = StateModel.objects.all()
    return Response(
      StateModelSerializer(
        states, context=self.get_serializer_context(), many=True
      ).data
    )

class CityAPI(generics.GenericAPIView):
  serializer_class = CityModelSerializer

# Get all cities in the db
  def get(self, *args, **kwargs):
    state_code = kwargs['state_code']
    cities = CityModel.objects.filter(state_code=state_code)
    return Response(
      CityModelSerializer(cities, context=self.get_serializer_context(), many=True
      ).data
    )