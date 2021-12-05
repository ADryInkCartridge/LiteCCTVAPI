# serializers.py
from rest_framework import serializers

from .models import Image
from .models import Token

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id','filename','imagedata','token')

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('id','token')