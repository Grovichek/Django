from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer, ProductReviewSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductReviewCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs['id']
        try:
            product = Product.objects.get(id=product_id)
            serializer.save(product=product)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED, content_type='application/json')
