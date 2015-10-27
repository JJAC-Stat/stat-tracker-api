from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.views import APIView

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer



# def basic(request):
#     return render(request, 'api/basic.html')
