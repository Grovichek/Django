from rest_framework import serializers
from .models import Basket
from app_product.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Basket
        fields = ('product', 'count')
