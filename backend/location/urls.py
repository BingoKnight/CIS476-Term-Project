from django.urls import path, include
from .api import StateAPI, CityAPI

urlpatterns = [
    path('getStates', StateAPI.as_view()),
    path('getCities/<str:state_code>', CityAPI.as_view())
]