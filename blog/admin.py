from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview','created_at', 'is_published', 'views_count')
    list_filter = ('title',)
    search_fields = ('title', 'content',)
