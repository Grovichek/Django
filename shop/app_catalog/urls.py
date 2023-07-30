from django.urls import path

from app_catalog.views import CategoriesView, CatalogView, PopularView, LimitedView, SalesView, BannersView

app_name = 'app_catalog'

urlpatterns = [

    path('categories/', CategoriesView.as_view(), name='categories'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('products/popular/', PopularView.as_view(), name='popular'),
    path('products/limited', LimitedView.as_view(), name='limited'),
    path('sales/', SalesView.as_view(), name='sales'),
    path('banners/', BannersView.as_view(), name='banners'),
]
