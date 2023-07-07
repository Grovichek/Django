from django.urls import path

from app_product.views import ProductView, ProductReviewView

app_name = 'app_product'

urlpatterns = [
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('product/<int:id>/review/', ProductReviewView.as_view(), name='product-review'),
]
