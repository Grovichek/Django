import random
from datetime import date

from django.core.paginator import EmptyPage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Count, Avg
from django.core.paginator import Paginator
from django.http import Http404

from app_product.models import Product
from app_product.serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer


# Эндпоинт для получения списка основных категорий
class CategoryListView(APIView):
    def get(self, request):
        main_categories = Category.objects.filter(parent_category=None)
        serializer = CategorySerializer(main_categories, many=True)
        return Response(serializer.data)


# Эндпоинт для просмотра каталога продуктов с фильтрами и пагинацией
class CatalogView(APIView):
    def get(self, request):
        # Извлечение фильтров из параметров запроса
        filters = {
            key.split('[', 1)[1].split(']')[0]: value
            for key, value in request.query_params.items()
            if key.startswith('filter[')
        }

        # Обработка фильтров
        name_filter = filters.get('name', '')
        min_price_filter = filters.get('minPrice', None)
        max_price_filter = filters.get('maxPrice', None)
        free_delivery_filter = filters.get('freeDelivery', False) == 'true'
        available_filter = filters.get('available', True) == 'true'
        category_filter = filters.get('category', None)
        sort_by = request.query_params.get('sort', 'date')
        sort_type = request.query_params.get('sortType', 'dec')

        # Запрос продуктов с предварительной загрузкой связанных данных
        products = Product.objects.select_related('category').prefetch_related(
            'productimage_set',
            'productreview_set',
            'productspecification_set',
            'producttag_set'
        ).all()

        # Применение фильтров к запросу продуктов
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

        # Применение сортировки к запросу продуктов
        if sort_by == 'rating':
            products = products.annotate(avg_rating=Avg('productreview__rate')).order_by('avg_rating')
        elif sort_by == 'price':
            products = products.order_by('price')
        elif sort_by == 'reviews':
            products = products.annotate(num_reviews=Count('productreview')).order_by('num_reviews')
        else:
            products = products.order_by('date')
        if sort_type == 'inc':
            products = products.reverse()

        # Инициализация пагинатора
        paginator = Paginator(products, request.query_params.get('limit', 20))
        page_number = request.query_params.get('currentPage', 1)
        try:
            current_page = paginator.page(page_number)
        except EmptyPage:
            raise Http404("No such page")


        # Сериализация и формирование ответа
        serializer = ProductSerializer(current_page, many=True)
        response_data = {
            'items': serializer.data,
            'currentPage': current_page.number,
            'lastPage': paginator.num_pages
        }
        return Response(response_data, status=status.HTTP_200_OK)


# Эндпоинт для получения популярных продуктов с высоким рейтингом и отзывами
class PopularProductsView(APIView):
    def get(self, request):
        popular_products = Product.objects.annotate(
            avg_rating=Avg('productreview__rate'),
            num_reviews=Count('productreview')
        ).filter(avg_rating__gt=4.5, num_reviews__gt=5)

        serializer = ProductSerializer(popular_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Эндпоинт для получения ограниченных продуктов
class LimitedProductsView(APIView):
    def get(self, request):
        limited_products = Product.objects.filter(limited=True)
        serializer = ProductSerializer(limited_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Эндпоинт для получения продуктов со скидкой
class SalesView(APIView):
    def get(self, request):
        today = date.today()
        sale_products = Product.objects.filter(
            date_from__lte=today, date_to__gt=today, sale_price__isnull=False
        ).order_by('sale_price')

        # Инициализация пагинатора
        paginator = Paginator(sale_products, request.query_params.get('limit', 20))
        page_number = request.query_params.get('currentPage', 1)

        try:
            current_page = paginator.page(page_number)
        except EmptyPage:
            raise Http404("No such page")

        # Сериализация и формирование ответа
        serializer = ProductSerializer(current_page, many=True)
        response_data = {
            'items': serializer.data,
            'currentPage': current_page.number,
            'lastPage': paginator.num_pages
        }
        return Response(response_data, status=status.HTTP_200_OK)


# Эндпоинт для получения баннеров
class BannersView(APIView):
    def get(self, request):

        all_banners = Product.objects.filter(count__gt=0)

        random_banners = random.sample(list(all_banners), 4)
        serializer = ProductSerializer(random_banners, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)