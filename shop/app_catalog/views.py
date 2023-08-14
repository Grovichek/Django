from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        main_categories = Category.objects.filter(parent_category=None)
        serializer = CategorySerializer(main_categories, many=True)
        return Response(serializer.data)


class CatalogView(APIView):
    ...


class PopularView(APIView):
    ...


class LimitedView(APIView):
    ...


class SalesView(APIView):
    ...


class BannersView(APIView):
    ...
