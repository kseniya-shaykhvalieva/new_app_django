from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published")
    success_url = reverse_lazy('blog:blog_list')
