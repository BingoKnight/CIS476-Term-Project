from django.db import models
from decimal import Decimal

# flight db layout
class FlightModel(models.Model):
  from_state    = models.CharField(max_length=20)
  from_city     = models.CharField(max_length=100)
  depart_date   = models.DateTimeField()

  to_state      = models.CharField(max_length=20)
  to_city       = models.CharField(max_length=100)

  cost          = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
  seats         = models.IntegerField(default=0)