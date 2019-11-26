from django.db import models

# city, state, zip
class FlightModel(models.Model):
  trip_type     = models.CharField(max_length=20)
  from_state    = models.CharField(max_length=20)
  from_city     = models.CharField(max_length=100)
  depart_date   = models.DateField()

  to_state      = models.CharField(max_length=20)
  to_city       = models.CharField(max_length=100)
  return_date   = models.DateField(null=True)

