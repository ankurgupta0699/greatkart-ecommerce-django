from django.shortcuts import render

from store import models as store_models

def home(request):
    products = store_models.Product.objects.filter(stock__gt=0)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
