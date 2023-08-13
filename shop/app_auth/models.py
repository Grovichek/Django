from os import path

from django.core.validators import RegexValidator
from django.db import models


def directory_path(instance, filename: str) -> str:
    return 'users/{username}/avatar/{filename}{extension}'.format(
        username=instance.username,
        filename=instance.avatar.count() + 1,
        extension=path.splitext(filename)[-1],
    )


phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")


class CustomUser(models.Model):
    name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=True, blank=True)
    avatar = models.ImageField(upload_to=directory_path, blank=True, null=True)

    def __str__(self):
        return self.username
