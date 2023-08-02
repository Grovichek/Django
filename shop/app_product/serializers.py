from rest_framework import serializers
from .models import Product, ProductImage, ProductReview, ProductSpecification


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(source='productimage_set', many=True)
    reviews = ProductReviewSerializer(source='productreview_set', many=True)
    specifications = ProductSpecificationSerializer(source='productspecification_set', many=True)

    class Meta:
        model = Product
        fields = '__all__'
