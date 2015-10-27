from rest_framework import serializers
from .models import Activity, DataPoint
from django.contrib.auth.models import User


class DataPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataPoint
        fields = ('activity', 'timestamp', 'value')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    datapoints = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #nested list
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'title', 'timestamp', 'datapoints', 'user')

# class DataPointSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DataPoint
#         fields = ('id', 'value', 'timestamp', 'activity')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'id', 'activities')
