# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '14/9/18 下午5:07'

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
from .views import BlogListView,BlogDetailView,BlogTypeView

urlpatterns = [
    url(r'all/$', BlogListView.as_view(), name="blogs"),
    url(r'(?P<blog_pk>\d+)/$',
        BlogDetailView.as_view(), name="blogs_detail"),
    url(r'types/(?P<blog_type>\d+)/$',
        BlogTypeView.as_view(), name="blogs_detail"),
]
