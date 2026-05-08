from django.shortcuts import get_object_or_404, redirect, render

from django.shortcuts import render

from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request,'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product" : product}
    return render(request, "product_detail.html", context)


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalog:home")
    else:
        form = ProductForm()
    return render(request, "product_form.html", {"form": form})
