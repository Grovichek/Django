from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Product, ProductTag, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer, ProductTagSerializer


# Класс для получения детальной информации о продукте по его идентификатору
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


# Класс для создания и получения отзывов о продукте
class ProductReviewView(APIView):
    # Получение отзывов о продукте
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            reviews = ProductReview.objects.filter(product=product)
            serializer = ProductReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    # Создание отзыва о продукте
    def post(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(product=product)
                redirect_url = reverse('app_product:product-reviews', kwargs={'id': id})
                return redirect(redirect_url)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


# Класс для получения списка тегов продуктов
class ProductTagListView(ListAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
