from django.urls import path

from app_profile.views import ProfileView, PasswordView, AvatarView

app_name = 'app_profile'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/password/', PasswordView.as_view(), name='password'),
    path('profile/avatar/', AvatarView.as_view(), name='avatar'),
]
