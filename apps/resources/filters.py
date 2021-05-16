# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '25/9/18 下午4:37'

import django_filters
from .models import SourcesCore


class SourcesCoreFilter(django_filters.rest_framework.FilterSet):
    """
    资源过滤类
    """
    sourcename=django_filters.CharFilter(field_name="sourcename",lookup_expr="icontains")

    class Meta:
        model = SourcesCore
        fields = ['question_type', 'sourcename']