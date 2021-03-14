# Product Serializer

# Django Rest Framework
from rest_framework import serializers

# Models
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serialize all the data in product model.
    """
    class Meta:
        """
        Meta Class.
        """
        model = Product
        fields = '__all__'