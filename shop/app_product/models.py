from os import path

from django.db import models


class Product(models.Model):
    category = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    full_description = models.TextField()
    free_delivery = models.BooleanField(default=False)
    rating = models.FloatField()

    def __str__(self):
        return self.title


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    return 'products/product_{pk}/images/{filename}{extension}'.format(
        pk=instance.product.id,
        filename=instance.product.productimage_set.count()+1,
        extension=path.splitext(filename)[-1],
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    src = models.ImageField(upload_to=product_images_directory_path)
    alt = models.CharField(max_length=200)

    def __str__(self):
        return self.alt


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    rate = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
