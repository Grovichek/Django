from django.urls import path

from app_basket.views import BasketView

app_name = 'app_basket'

urlpatterns = [
    path('basket/', BasketView.as_view(), name='basket')
]
