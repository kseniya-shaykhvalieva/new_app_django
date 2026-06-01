from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductsCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/',ContactsTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60*15)(ProductDetailView.as_view()), name='product_detail'),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/products_category/", ProductsCategoryView.as_view(), name="products_category"),
]
