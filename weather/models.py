from django.db import models

# models.py

from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
