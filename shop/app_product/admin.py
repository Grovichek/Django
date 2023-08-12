from django.contrib import admin
from app_product.models import Product, ProductImage, ProductReview, ProductSpecification, ProductTag


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductReviewInline(admin.StackedInline):
    model = ProductReview
    extra = 1


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification
    extra = 1


class ProductTagInline(admin.TabularInline):
    model = ProductTag.product.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductReviewInline,
        ProductSpecificationInline,
        ProductTagInline,
    ]


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    exclude = ('product',)
