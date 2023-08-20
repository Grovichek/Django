import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer


# Получение профиля пользователя.
def get_user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return user_profile



# Вход пользователя в систему.
@csrf_protect
def sign_in(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Sign-in successful."})
        else:
            return JsonResponse({"message": "Sign-in error."}, status=400)
    return JsonResponse({"message": "Method not supported."}, status=405)


# Регистрация нового пользователя.
@csrf_protect
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = name
            user.save()

            user_profile = UserProfile.objects.create(user=user, fullName=name, email=email)
            serializer = UserProfileSerializer(user_profile)

            login(request, user)

            return JsonResponse(serializer.data, status=201)
        except IntegrityError:
            return JsonResponse({"message": "User with this username or email already exists."}, status=400)

    return JsonResponse({"message": "Method not supported."}, status=405)


# Выход пользователя из системы.
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"message": "User successfully signed out."})
    return JsonResponse({"message": "Method not supported."}, status=405)


# Профиль пользователя.
@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileView(APIView):
    def get(self, request):
        user_profile = get_user_profile(request)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def post(self, request):
        user_profile = get_user_profile(request)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Обновление аватара пользователя.
@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileAvatarView(APIView):
    def post(self, request):
        if request.method == 'POST':
            image_data = request.FILES.get('avatar')
            new_avatar_alt = request.POST.get('alt')

            if image_data:
                user_profile = get_user_profile(request)
                user_profile.avatar = image_data
                user_profile.avatar.alt = new_avatar_alt
                user_profile.save()

                return Response({
                    "src": user_profile.avatar.url,
                    "alt": new_avatar_alt
                })
            else:
                return Response({"message": "Invalid image data."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Method not supported."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ProfilePasswordView(APIView):
    def post(self, request):
        print(request.body)  # TODO с фронта приходит пустая строка вместо нового пароля
        return Response({"message": "frontend error."}, status=400)
