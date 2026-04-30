from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Изображение", help_text="Загрузите изображение"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="products")
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category", "name"]
