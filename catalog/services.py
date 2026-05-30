from django.shortcuts import get_object_or_404

from catalog.models import Product


def products_category(pk):
    """Возвращает список всех продуктов в указанной категории"""
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.filter(category=product.category)
    return products
