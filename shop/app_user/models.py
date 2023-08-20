from os import path

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


def directory_path(instance, filename: str) -> str:
    return 'users/{username}/avatar/{filename}_avatar{extension}'.format(
        username=instance.user.username,
        filename=instance.user.username,
        extension=path.splitext(filename)[-1],
    )


phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(default='No name', max_length=20)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=True, blank=True)
    avatar = models.ImageField(upload_to=directory_path, blank=True, null=True)

    def __str__(self):
        return self.user.username
