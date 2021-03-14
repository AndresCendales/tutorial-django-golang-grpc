# Urls

# Django Rest Framework
from django.contrib import admin
from django.urls import path
from rest_framework import routers

# Viewsets
from products.views import ProductModelViewSet

router = routers.SimpleRouter()
router.register(r'products' , ProductModelViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += router.urls
