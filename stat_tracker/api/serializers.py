from rest_framework import serializers
from .models import Activity, DataPoint

class DataPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataPoint
        fields = ('activity', 'timestamp', 'value')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    DataPoint_set = DataPointSerializer(many=True, read_only=True) #nested list

    class Meta:
        model = Activity
        fields = ('id', 'title', 'timestamp', 'datapoints')
