from rest_framework import serializers
from .models import Activity, DataPoint

class DataPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataPoint
        fields = ('activity', 'timestamp', 'value')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    data = DataPointSerializer(many=True, read_only=True) #nested list
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'title', 'timestamp', 'data', 'user')

# class DataPointSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DataPoint
#         fields = ('id', 'value', 'timestamp', 'activity')
