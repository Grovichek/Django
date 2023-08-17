from django.urls import path

from app_product.views import ProductDetailView, ProductReviewView, ProductTagListView

app_name = 'app_product'

urlpatterns = [
    path('product/<int:id>/', ProductDetailView.as_view(), name='product'),
    path('product/<int:id>/reviews/', ProductReviewView.as_view(), name='product-reviews'),

    path('tags/', ProductTagListView.as_view(), name='tags'),
]
