from django.urls import path

from app_product.views import ProductDetailView, ProductReviewCreateView, ProductTagListView

app_name = 'app_product'

urlpatterns = [
    path('product/<int:id>/', ProductDetailView.as_view(), name='product'),
    path('product/<int:id>/reviews/', ProductReviewCreateView.as_view(), name='product-review'),

    path('tags/', ProductTagListView.as_view(), name='tags'),
]
