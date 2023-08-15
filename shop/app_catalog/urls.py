from django.urls import path

from app_catalog.views import CategoryListView, CatalogView, PopularProductsView, LimitedProductsView, SalesView, BannersView

app_name = 'app_catalog'

urlpatterns = [

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('products/popular/', PopularProductsView.as_view(), name='popular'),
    path('products/limited/', LimitedProductsView.as_view(), name='limited'),
    path('sales/', SalesView.as_view(), name='sales'),
    path('banners/', BannersView.as_view(), name='banners'),
]
