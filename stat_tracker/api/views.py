from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity, DataPoint
from .serializers import ActivitySerializer, DataPointSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .permissions import IsAskerOrReadOnly, IsReadOnly
from rest_framework.decorators import detail_route, api_view
from rest_framework import viewsets, permissions, status

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAskerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self):
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

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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
          activity_id = self.kwargs['activity_id']
          get_object_or_404(Activity, pk=activity_id)
          serializer.save(activity=Activity.objects.get(pk=activity_id))

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

@api_view(['GET'])
def whoami(request):
    user = request.user
    if user.is_authenticated():
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response('', status=status.HTTP_404_NOT_FOUND)

def basic(request):
    return render(request, 'api/basic.html')
