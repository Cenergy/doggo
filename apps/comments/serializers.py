# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '25/9/18 上午9:35'


# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '10/8/18 下午4:26'


from rest_framework import serializers

from .models import Suggestion,FriendLinks

class  SuggestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields="__all__"
class  FriendLinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = FriendLinks
        fields="__all__"

