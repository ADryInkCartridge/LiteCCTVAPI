# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'image', views.ImageViewSet)
router.register(r'token', views.TokenViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='home'),
    path('my-images/', views.ViewImage, name='my-images'),
    path('tokenCheck/', views.CheckToken)
]