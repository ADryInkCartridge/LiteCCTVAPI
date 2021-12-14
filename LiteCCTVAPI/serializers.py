# serializers.py
from rest_framework import serializers

from LiteCCTVAPI.AI.face_detector import getFacesFromImage

from .models import FaceImage, Image
from .models import Token

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id','filename','imagedata','token')
    
    def create(self, validated_data):
        image = Image.objects.create(**validated_data)
        detected_faces = getFacesFromImage(validated_data['imagedata'])
        for d in detected_faces:
            face_image = FaceImage.objects.create(image_data=d[0], image_emotion=d[1], image_id=image)
        return image

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('id','token')