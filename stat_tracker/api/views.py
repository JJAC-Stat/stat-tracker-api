from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity, DataPoint
from .serializers import ActivitySerializer, DataPointSerializer
from rest_framework.views import APIView


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer


def basic(request):
    return render(request, 'api/basic.html')
# class DataPointViewSet(viewsets.ModelViewSet):
#     queryset = DataPoint.objects.all()
#     serializer_class = DataPointSerializer
