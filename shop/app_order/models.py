from django.db import models
from django.contrib.auth.models import User

from app_product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fullName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    delivery_type = models.CharField(max_length=10, blank=True)
    payment_type = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=10, default='in process')
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    products = models.ManyToManyField(Product, through='OrderProduct', related_name='orders')

    def __str__(self):
        return f"Order {self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order.id} - Product {self.product.id}"
