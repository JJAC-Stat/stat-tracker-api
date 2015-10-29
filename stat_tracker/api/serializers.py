from rest_framework import serializers
from .models import Activity, DataPoint
from django.contrib.auth.models import User


class DataPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataPoint
        fields = ('id', 'activity', 'timestamp', 'value')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    datapoints = DataPointSerializer(many=True, read_only=True) #nested list
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'user', 'title', 'timestamp', 'datapoints')

# class DataPointSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DataPoint
#         fields = ('id', 'value', 'timestamp', 'activity')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'password', 'activities')
