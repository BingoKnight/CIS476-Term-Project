from django.db import models

class StateModel(models.Model):
  state_code   = models.CharField(max_length=2)

class CityModel(models.Model):
  state_code   = models.CharField(max_length=2)
  city_name   = models.CharField(max_length=100)