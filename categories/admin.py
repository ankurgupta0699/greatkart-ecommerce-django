from django.contrib import admin

from categories import models as categories_models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }
    list_display = ('name', 'slug',)


admin.site.register(categories_models.Category, CategoryAdmin)
