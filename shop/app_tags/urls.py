from django.urls import path

from app_tags.views import TagsView

app_name = 'app_tags'

urlpatterns = [
    path('tags/', TagsView.as_view(), name='tags'),
]
