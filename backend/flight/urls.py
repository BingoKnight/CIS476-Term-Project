from django.urls import path, include
from .views import get_flight_list, get_all

urlpatterns = [
  path(r'', get_all),
  path(r'getFlights', get_flight_list),
]