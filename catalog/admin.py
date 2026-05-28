from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'category', 'created_at', 'updated_at', 'owner',
                    'is_published',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)
    search_fields = ('name',)
