from itertools import product
from unicodedata import category
from django.shortcuts import get_object_or_404, render

from categories import models as categories_models
from store import models as store_models


def store(request, category_slug=None):
    products = None

    if category_slug != None:
        category = get_object_or_404(categories_models.Category, slug=category_slug)
        products = store_models.Product.objects.filter(category=category, stock__gt=0)
    else:
        products = store_models.Product.objects.filter(stock__gt=0)
    
    context = {
        'products': products,
        'products_count': products.count(),
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(store_models.Product, category__slug=category_slug, slug=product_slug)

    context = {
        'product': product,
    }
    
    return render(request, 'store/product-detail.html', context)
