"""stat_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from api.views import ActivityViewSet, DataPointViewSet, UserViewSet
from api.views import month_chart
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'activities/(?P<activity_id>\d*)/stats', DataPointViewSet)
#router.register(r'datapoints', DataPointViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', 'api.views.basic',name='basic' ),
    url(r'^api/activities/(?P<activity_id>\d+)/graph', month_chart)
]
