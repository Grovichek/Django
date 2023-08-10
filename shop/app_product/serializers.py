from rest_framework import serializers
from .models import Product, ProductImage, ProductReview, ProductSpecification


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('src', 'alt')


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ('author', 'email', 'text', 'rate', 'date')


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = ('name', 'value')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(source='productimage_set', many=True)
    reviews = ProductReviewSerializer(source='productreview_set', many=True)
    specifications = ProductSpecificationSerializer(source='productspecification_set', many=True)

    class Meta:
        model = Product
        fields = (
        'id', 'category', 'price', 'count', 'date', 'title', 'description', 'full_description', 'free_delivery',
        'images', 'reviews', 'specifications', 'rating')
