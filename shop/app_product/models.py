from os import path

from django.db import models


def directory_path(instance, filename: str) -> str:
    return 'products/{title}/images/{filename}{extension}'.format(
        title=instance.product.title,
        filename=instance.product.productimage_set.count() + 1,
        extension=path.splitext(filename)[-1],
    )


class Product(models.Model):
    category = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    full_description = models.TextField(max_length=2000)
    free_delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    src = models.ImageField(upload_to=directory_path)
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
