from django.db import models

class StateModel(models.Model):
  id    = models.IntegerField(primary_key=True)
  name  = models.CharField(max_length=20)

class CityModel(models.Model):
  id        = models.IntegerField(primary_key=True)
  state_id  = models.IntegerField()
  name      = models.CharField(max_length=100)