from django.contrib import admin

from app_product.models import Product, ProductImage, ProductReview, ProductSpecification


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductReviewInline(admin.StackedInline):
    model = ProductReview


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductReviewInline,
        ProductSpecificationInline,
    ]
