# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '25/9/18 上午9:35'


# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '10/8/18 下午4:26'


from rest_framework import serializers

from .models import SourcesCore,Gallery,Photos

###SourcesCore

class  SourcesCoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = SourcesCore
        fields="__all__"



class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields="__all__"
