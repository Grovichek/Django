from django.contrib import admin
from app_product.models import Product, ProductImage, ProductReview, ProductSpecification, ProductTag


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductReviewInline(admin.StackedInline):
    model = ProductReview
    extra = 1
    classes = ('collapse',)


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification
    extra = 1
    classes = ('collapse',)


class ProductTagInline(admin.TabularInline):
    model = ProductTag.product.through
    extra = 1
    classes = ('collapse',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductReviewInline,
        ProductSpecificationInline,
        ProductTagInline,
    ]

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'price',),
        }),
        ('Sale', {
            'classes': ('collapse',),
            'fields': ('sale_price', 'date_from', 'date_to'),
        }),
        (None, {
            'fields': ('count', 'description', 'full_description', 'free_delivery',),
        }),
    )


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    exclude = ('product',)
