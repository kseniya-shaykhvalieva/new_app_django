from django.shortcuts import get_object_or_404

from catalog.models import Product
from config.settings import CACHES
from django.core.cache import cache


def products_category(pk):
    """Возвращает список всех продуктов в указанной категории"""
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.filter(category=product.category)
    return products


def get_products_from_cache():
    """Низкоуровневое кеширование для списка продуктов"""
    if not CACHES:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products, 60 * 15)
    return products
