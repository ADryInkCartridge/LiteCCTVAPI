from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ImageSerializer,TokenSerializer
from .models import Image,Token
from django.template import loader
import json
import random, string

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('filename')
    serializer_class = ImageSerializer

    
class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all().order_by('token')
    serializer_class = TokenSerializer

def ViewImage(request):

    if request.method == 'GET':
        return HttpResponse("Please use POST method")
    elif request.method == 'POST':
        images = Image.objects.filter(token=request.POST['token']).order_by('filename')
        template = loader.get_template('./images.html')
        context = {
            'images': images,
        }
        return HttpResponse(template.render(context, request))
    

def CheckToken(request):
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    print(x)
    tokens = Token.objects.filter(token=x).exists()
    while(tokens==True):
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        print(x)
        tokens = Token.objects.filter(token=x).exists()
    token_instance = Token.objects.create(token=x)
    return HttpResponse(x)

def index(request):
    return render(request,'./index.html', {})