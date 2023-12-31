from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from decimal import Decimal

from app_product.models import Product
from .models import Order, OrderProduct
from .serializers import OrderSerializer


# Представление для создания заказа.
class OrderView(APIView):
    def post(self, request):
        # Получаем данные о продуктах
        products_data = request.data
        total_cost = Decimal()

        # Создаем заказ
        order = Order.objects.create(status='Created')

        # Добавляем продукты к заказу
        for product_data in products_data:
            product = get_object_or_404(Product, id=product_data['id'])
            OrderProduct.objects.create(
                order=order,
                product=product,
                count=product_data['count']
            )

            total_cost += product.price * product_data['count']

        # Устанавливаем общую стоимость заказа
        order.total_cost = total_cost
        order.save()

        return Response({'orderId': order.id}, status=status.HTTP_201_CREATED)


    def get(self, request):
        # Получаем заказы пользователя, который авторизован
        orders = Order.objects.filter(user=request.user)

        # Сериализуем заказы
        serializer = OrderSerializer(orders, many=True)
        print(serializer.data)

        return Response(serializer.data)


# Представление для просмотра и обновления заказа.
class OrderDetailView(APIView):
    def get(self, request, order_id):
        # Получаем заказ по ID
        order = get_object_or_404(Order, id=order_id)

        # Обновляем данные из профиля пользователя, если авторизован
        if request.user.is_authenticated:
            order.fullName = request.user.userprofile.fullName
            order.email = request.user.userprofile.email
            order.phone = request.user.userprofile.phone
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request, order_id):
        # Получаем заказ по ID
        order = get_object_or_404(Order, id=order_id)
        try:
            # Обновляем данные заказа из запроса
            order.delivery_type = request.data.get('deliveryType', order.delivery_type)
            order.payment_type = request.data.get('paymentType', order.payment_type)
            order.city = request.data.get('city', order.city)
            order.address = request.data.get('address', order.address)
            order.total_cost = request.data.get('total_cost', order.total_cost)
            order.user = request.user

            order.status = 'Accepted'

            order.save()

            return Response({'orderId': order.id}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
