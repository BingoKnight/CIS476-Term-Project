from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from .models import FlightModel
from .serializers import FlightModelSerializer
from rest_framework.decorators import api_view
import datetime

# Get the list of all flights in the database, for debugging purposes
@api_view(['GET'])
def get_all(request):
  data = FlightModel.objects.all()
  serializer = FlightModelSerializer(data, many=True)
  return JsonResponse(serializer.data, safe=False)


# Get list of flights that match request criteria such as:
# the to and from locations, the dates of depature and arrival, and one way or round trip
@api_view(['POST'])
def get_flight_list(request):
  return_queryset = None

  print('request recieved')
  depart_date = datetime.datetime.strptime(request.data['depart'], '%Y-%m-%d')

  print('querying from location')
  outbound_queryset = FlightModel.objects.filter(from_state=request.data['fromState'],
                                    from_city=request.data['fromCity'],
                                    depart_date=datetime.datetime(
                                      depart_date.year, 
                                      depart_date.month,
                                      depart_date.day)
                                    ).order_by('cost')
  
  if 'toState' in request.data and request.data['toState'] and 'toCity' in request.data and request.data['toCity']:
    outbound_queryset = outbound_queryset.filter(to_state=request.data['toState'], to_city=request.data['toCity'])

  print(outbound_queryset)

  if request.data['tripType'] == 'RT':
    print('querying to location')
    return_date = datetime.datetime.strptime(request.data['return'], '%Y-%m-%d')
    return_queryset = FlightModel.objects.filter(to_state=request.data['fromState'],
                                    to_city=request.data['fromCity'],
                                    depart_date=datetime.datetime(
                                      return_date.year, 
                                      return_date.month,
                                      return_date.day)
                                    ).order_by('cost')
    
    if 'toState' in request.data and request.data['toState'] and 'toCity' in request.data and request.data['toCity']:
      return_queryset = return_queryset.filter(from_state=request.data['toState'], from_city=request.data['toCity'],)

    for row in return_queryset:
      row.depart_date = row.depart_date.strftime("%m-%d-%Y")

  for row in outbound_queryset:
    row.depart_date = row.depart_date.strftime("%m-%d-%Y")

  outbound_serializer = FlightModelSerializer(outbound_queryset, many=True)
  return_serializer = FlightModelSerializer(return_queryset, many=True)
  
  print('Done!')
  return JsonResponse(
    {
      "outbound": outbound_serializer.data, 
      "return": return_serializer.data
    }, 
    safe=False
  )