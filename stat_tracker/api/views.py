from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.views import APIView

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

<<<<<<< HEAD
=======

>>>>>>> 7f99ef66c1d8e03a64c96c83d3eb364fbdc71e4e

def basic(request):
    return render(request, 'api/basic.html')

def create(self, validated data):


class UserViewSet(viewsets.ModelViewset):
    queryset = User.objects.all()
    serilalizer_class = UserSerializer
