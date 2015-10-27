from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity, DataPoint
from .serializers import ActivitySerializer, DataPointSerializer
from rest_framework.views import APIView

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# class DataPointViewSet(viewsets.ModelViewSet):
#     queryset = DataPoint.objects.all()
#     serializer_class = DataPointSerializer



def basic(request):
     return render(request, 'api/basic.html')
