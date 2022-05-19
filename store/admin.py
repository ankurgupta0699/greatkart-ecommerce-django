from django.contrib import admin
from django.utils.html import format_html

from store import models as store_models


class ProductAdmin(admin.ModelAdmin):
    def product_image(self, obj):
        return format_html('<img src="{}" width="70px"/>'.format(obj.images.url))
    
    list_display = ('name', 'product_image', 'price', 'stock', 'category', 'updated_at')
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(store_models.Product, ProductAdmin)
