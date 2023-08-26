from django.urls import path

from app_user.views import sign_in, sign_up, sign_out, ProfileView, ProfilePasswordView, ProfileAvatarView

app_name = 'app_user'

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),
    path('sign-out/', sign_out, name='sign-out'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/password/', ProfilePasswordView.as_view(), name='profile-password'),
    path('profile/avatar/', ProfileAvatarView.as_view(), name='profile-avatar'),
]
