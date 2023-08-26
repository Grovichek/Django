from django.contrib import admin
from .models import UserProfile

# TODO Удалить перед сдачей
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullName', 'email', 'phone')
