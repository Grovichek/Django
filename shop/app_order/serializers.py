from rest_framework import serializers

from .models import Order, OrderProduct
from app_product.serializers import ProductSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'count')


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id', 'created_at', 'fullName', 'email', 'phone', 'delivery_type', 'payment_type',
            'total_cost', 'status', 'city', 'address', 'products'
        )

    def get_products(self, obj):
        products = obj.orderproduct_set.all()
        serialized_products = []

        for product in products:
            serialized_product = ProductSerializer(product.product).data
            serialized_product['count'] = product.count
            serialized_products.append(serialized_product)

        return serialized_products
