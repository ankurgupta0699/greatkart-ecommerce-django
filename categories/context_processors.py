from categories import models as categories_models


def category_links(request):
    categories = categories_models.Category.objects.all()
    return dict(categories=categories)
