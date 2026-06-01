from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты из фикстуры'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'categories_fixture.json')
        call_command('loaddata', 'products_fixture.json')

        self.stdout.write(self.style.SUCCESS('Данные из фикстур успешно загружены'))
