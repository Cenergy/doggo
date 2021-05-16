# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '14/9/18 下午5:07'

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from resources import views

from .views import SourcesCoreViewset

router = DefaultRouter()

router.register(r'v1/sources2', SourcesCoreViewset, basename='sources')

urlpatterns = [
    url(r'resources/$', views.SourcesList.as_view(), name="resources"),
    url(r'sources/$', views.SourcesListView.as_view(), name="sources"),
]