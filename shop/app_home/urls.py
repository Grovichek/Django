from django.urls import path

from app_home.views import IndexView

app_name = 'app_home'

urlpatterns = [
    path('/', IndexView.as_view(), name='index'),

]
