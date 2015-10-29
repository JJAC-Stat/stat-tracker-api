from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity, DataPoint
from .serializers import ActivitySerializer, DataPointSerializer, UserSerializer
from rest_framework import viewsets, permissions
from .permissions import IsUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    #permission_classes = IsUser

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        pass
    #     activity_id = self.kwargs['activity_pk']
    #     get_object_or_404(Activity, pk=activity_id)
    #     return self.queryset.filter(activity_id=activity_id)
    #
    # def get_serializer_context(self):
    #     context = super().get_serializer_context().copy()
    #     context['activity_pk'] = self.kwargs['activity_pk']
    #     return context


class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

    #permission_classes = IsUser

    def get_queryset(self):
        activity_id = self.kwargs['activity_id']
        get_object_or_404(Activity, pk=activity_id)
        return self.queryset.filter(activity=activity_id)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['activity_id'] = self.kwargs['activity_id']
        return context
        # return {'question_pk': self.kwargs['question_pk']}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = IsUser
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


def basic(request):
    return render(request, 'api/basic.html')
