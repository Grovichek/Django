from os import path

from django.db import models


def directory_path(instance, filename: str) -> str:
    if instance.parent_category is None:
        my_path = 'categories/{title}/{filename}{extension}'
    else:
        my_path = 'categories/{parent_category}/{title}/{filename}{extension}'

    return my_path.format(
        title=instance.title,
        filename=instance.alt_text,
        extension=path.splitext(filename)[-1],
        parent_category=instance.parent_category
    )


class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategories',
        limit_choices_to={'parent_category__isnull': True},
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=directory_path)
    alt_text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title
