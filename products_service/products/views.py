# Products Views

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet

# Models
from products.models import Product

# Serializer
from products.serializer import ProductSerializer


class ProductModelViewSet(ModelViewSet):
    """
    View to handle CRUD of products
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
