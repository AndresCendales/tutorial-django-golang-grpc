# Models for products

from django.db import models


class Product(models.Model):
    """
    Products define the model for all products in the e-commerce
    """
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    price = models.FloatField(
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
