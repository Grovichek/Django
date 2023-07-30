from django.urls import path

from app_order.views import OrderListView, OrderDetailView

app_name = 'app_order'

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/<int:id>', OrderDetailView.as_view(), name='order'),
]
