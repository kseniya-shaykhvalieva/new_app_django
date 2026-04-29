from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='Категория1')

        products = [
            {'name':'Лук', 'description':'Ядрёный', 'category':category, 'price':50},
            {'name':'Свекла', 'category':category, 'price':35},
            {'name': 'Баклажан', 'description': 'Фиолетовый', 'category': category, 'price': 74},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт {product.name} уже существует'))
