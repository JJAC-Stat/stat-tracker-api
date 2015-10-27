from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=150)
    timestamp = models.DateField()
    user = models.ForeignKey(User)
    units = models.CharField(max_length=15, null=True)

class DataPoint(models.Model):
    activity = models.ForeignKey(Activity, related_name='datapoints')
    timestamp = models.DateField()
    value = models.PositiveSmallIntegerField()
