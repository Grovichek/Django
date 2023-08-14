from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    subcategories = serializers.SerializerMethodField()

    def get_subcategories(self, obj):
        subcategories = Category.objects.filter(parent_category=obj)
        serializer = CategorySerializer(subcategories, many=True)
        return serializer.data

    def get_image(self, category):
        return {
            "src": category.image.url,
            "alt": category.alt_text
        }

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'alt_text', 'subcategories')
