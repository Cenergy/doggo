# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '6/8/18 下午2:45'

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

from .views import SuggestionsView



urlpatterns = [
    url(r'v1/suggestions/', csrf_exempt(SuggestionsView.as_view()),
        name="suggestions"),
]
