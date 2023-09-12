from django.urls import path

from app_order.views import OrderView, OrderDetailView

app_name = 'app_order'

urlpatterns = [
    path('orders/', OrderView.as_view(), name='orders'),
    path('order/<int:order_id>/', OrderDetailView.as_view(), name='order'),
]
