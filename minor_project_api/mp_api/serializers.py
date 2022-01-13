import string

from rest_framework import serializers
from . import models

'''class FollowListSerializer(serializers.Serializer):
    followList = serializers.ListSerializer(type=string)'''
class SentimentSerializer(serializers.Serializer):
    neg = serializers.FloatField()
    neu = serializers.FloatField()
    pos = serializers.FloatField()
    compound = serializers.FloatField()