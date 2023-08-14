from app_product.models import Product
from app_product.serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer
from django.core.paginator import EmptyPage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import Http404


class CategoryListView(APIView):
    def get(self, request):
        main_categories = Category.objects.filter(parent_category=None)
        serializer = CategorySerializer(main_categories, many=True)
        return Response(serializer.data)


class CatalogView(APIView):
    def get(self, request):
        filters = {
            key.split('[', 1)[1].split(']')[0]: value
            for key, value in request.query_params.items()
            if key.startswith('filter[')
        }

        name_filter = filters.get('name', '')
        min_price_filter = filters.get('minPrice', None)
        max_price_filter = filters.get('maxPrice', None)
        free_delivery_filter = filters.get('freeDelivery', False) == 'true'
        available_filter = filters.get('available', True) == 'true'
        category_filter = filters.get('category', None)
        sort_by = request.query_params.get('sort', 'date')
        sort_type = request.query_params.get('sortType', 'dec')
        tags_filter = request.query_params.getlist('tags')

        products = Product.objects.select_related('category').prefetch_related(
            'productimage_set',
            'productreview_set',
            'productspecification_set',
            'producttag_set'
        ).all()

        if name_filter:
            products = products.filter(Q(title__icontains=name_filter) | Q(description__icontains=name_filter))

        if min_price_filter:
            products = products.filter(price__gte=min_price_filter)

        if max_price_filter:
            products = products.filter(price__lte=max_price_filter)

        if free_delivery_filter:
            products = products.filter(free_delivery=True)

        if available_filter:
            products = products.exclude(count=0)

        if category_filter and category_filter != 'NaN':
            products = products.filter(category=category_filter)

        if sort_by == 'rating':
            products = products.order_by('-productreview__rate')
        elif sort_by == 'price':
            products = products.order_by('price')
        elif sort_by == 'reviews':
            products = products.annotate(num_reviews=Count('productreview')).order_by('-num_reviews')
        else:
            products = products.order_by('-date')
        if sort_type == 'inc':
            products = products.reverse()

        paginator = Paginator(products, request.query_params.get('limit', 20))
        page_number = request.query_params.get('currentPage', 1)

        try:
            current_page = paginator.page(page_number)
        except EmptyPage:
            raise Http404("No such page")

        serializer = ProductSerializer(current_page, many=True)
        response_data = {
            'items': serializer.data,
            'currentPage': current_page.number,
            'lastPage': paginator.num_pages
        }
        return Response(response_data, status=status.HTTP_200_OK)


class PopularView(APIView):
    ...


class LimitedView(APIView):
    ...


class SalesView(APIView):
    ...


class BannersView(APIView):
    ...
