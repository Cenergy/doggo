# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '25/9/18 上午9:35'


# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '10/8/18 下午4:26'


from rest_framework import serializers
from .models import Blog
###SourcesCore


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields="__all__"