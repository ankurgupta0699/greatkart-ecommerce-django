from django.urls import path

from store import views as store_views


urlpatterns = [
    path('', store_views.store, name='store'),
    path('<slug:category_slug>/', store_views.store, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', store_views.product_detail, name='product_detail'),
]
