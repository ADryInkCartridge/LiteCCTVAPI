from django.contrib import admin
from .models import Image,Token,FaceImage

admin.site.register(Image)
admin.site.register(Token)
admin.site.register(FaceImage)