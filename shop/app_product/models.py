from os import path

from django.db import models
from django.db.models import SET_NULL
from transliterate import translit

from app_catalog.models import Category


def translate_path(text):
    return translit(text, 'ru', reversed=True).replace(' ', '_')


def directory_path(instance, filename: str) -> str:
    if instance.product.category.parent_category is None:
        my_path = 'categories/{category}/{title}/images/{filename}{extension}'
    else:
        my_path = 'categories/{parent_category}/{category}/{title}/images/{filename}{extension}'

    return translate_path(my_path.format(
        parent_category=instance.product.category.parent_category,
        category=instance.product.category,
        title=instance.product.title,
        filename=instance.product.productimage_set.count() + 1,
        extension=path.splitext(filename)[-1],
    ))


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    full_description = models.TextField(max_length=2000)
    free_delivery = models.BooleanField(default=False)
    limited = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    src = models.ImageField(upload_to=directory_path, max_length=500)
    alt = models.CharField(max_length=200)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    rate = models.IntegerField(default=5)
    date = models.DateTimeField(auto_now_add=True)


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class ProductTag(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
