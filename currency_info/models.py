from django.db import models


class Currency(models.Model):
  name = models.CharField(max_length=50)
  rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
