from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Превью", help_text="Загрузите изображение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "заголовок"
        verbose_name_plural = "заголовки"
        ordering = ["title", "created_at"]
