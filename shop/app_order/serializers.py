from rest_framework import serializers

from .models import Order, OrderProduct
from app_product.serializers import ProductSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'count')


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    createdAt = serializers.DateTimeField(source='created_at', format='%Y-%m-%d %H:%M')
    deliveryType = serializers.CharField(source='delivery_type')
    paymentType = serializers.CharField(source='payment_type')
    totalCost = serializers.DecimalField(max_digits=10, decimal_places=2, source='total_cost')

    class Meta:
        model = Order
        fields = (
            'id', 'createdAt', 'fullName', 'email', 'phone', 'deliveryType', 'paymentType',
            'totalCost', 'status', 'city', 'address', 'products'
        )

    def get_products(self, obj):
        products = obj.orderproduct_set.all()
        serialized_products = []

        for product in products:
            serialized_product = ProductSerializer(product.product).data
            serialized_product['count'] = product.count
            serialized_products.append(serialized_product)

        return serialized_products
