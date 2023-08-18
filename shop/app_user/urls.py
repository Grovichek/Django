from django.urls import path

from app_user.views import sign_in, sign_up, sign_out, ProfileView, ProfilePasswordView, ProfileAvatarView

app_name = 'app_user'

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),         # Эндпоинт для входа пользователя
    path('sign-up/', sign_up, name='sign-up'),         # Эндпоинт для регистрации пользователя
    path('sign-out/', sign_out, name='sign-out'),      # Эндпоинт для выхода пользователя

    path('profile/', ProfileView.as_view(), name='profile'),                      # Эндпоинт для просмотра и обновления профиля
    path('profile/password/', ProfilePasswordView.as_view(), name='profile-password'),  # Эндпоинт для обновления пароля
    path('profile/avatar/', ProfileAvatarView.as_view(), name='profile-avatar'),      # Эндпоинт для обновления аватара
]

