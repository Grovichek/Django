from os import path

from django.db import models
from transliterate import translit


def translate_path(text):
    return translit(text, 'ru', reversed=True).replace(' ', '_')


def directory_path(instance, filename: str) -> str:
    if instance.parent_category is None:
        my_path = 'categories/{title}/{title}{extension}'
    else:
        my_path = 'categories/{parent_category}/{title}/{title}{extension}'

    return translate_path(my_path.format(
        title=instance.title,
        extension=path.splitext(filename)[-1],
        parent_category=instance.parent_category
    ))


class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='categories',
        limit_choices_to={'parent_category__isnull': True},
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=directory_path)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
