from django.urls import path

from app_order.views import OrderCreateView, OrderDetailView

app_name = 'app_order'

urlpatterns = [
    path('orders/', OrderCreateView.as_view(), name='orders'),
    path('order/<int:order_id>/', OrderDetailView.as_view(), name='order'),
]
