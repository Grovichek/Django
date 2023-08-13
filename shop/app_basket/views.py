from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Basket
from .serializers import BasketSerializer
from app_product.models import Product

class BasketView(APIView):
    def get(self, request):
        basket_items = Basket.objects.all()
        serializer = BasketSerializer(basket_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.data.get('id')
        count = request.data.get('count')

        try:
            product = Product.objects.get(id=product_id)
            basket_item, created = Basket.objects.get_or_create(product=product)
            basket_item.count = count
            basket_item.save()
            serializer = BasketSerializer(basket_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product_id = request.data.get('product_id')

        try:
            product = Product.objects.get(id=product_id)
            Basket.objects.filter(product=product).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
