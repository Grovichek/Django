from django.urls import path

from app_auth.views import SignUpView, SignInView, SignOutView

app_name = 'app_auth'

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
]
