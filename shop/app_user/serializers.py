from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.user.email

    def get_avatar(self, obj):
        return {
            "src": obj.avatar.url if obj.avatar else None,
            "alt": obj.fullName
        }

    class Meta:
        model = UserProfile
        fields = ('fullName', 'email', 'phone', 'avatar', 'email')
