from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=150)
    timestamp = models.DateField()
    user = models.ForeignKey(User, related_name='activities')
    units = models.CharField(max_length=15, null=True)

    def __str__(self):
        return '{}:{}'.format(self.title, self.datapoints)

class DataPoint(models.Model):
    activity = models.ForeignKey(Activity, related_name='datapoints')
    timestamp = models.DateField()
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}:{} @ {}'.format(self.activity, self.value, self.timestamp)
