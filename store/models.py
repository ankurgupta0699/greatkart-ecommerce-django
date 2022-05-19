from django.db import models
from django.urls import reverse

from categories import models as categories_models


class Product(models.Model):
    name = models.TextField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.PositiveIntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(categories_models.Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.name
