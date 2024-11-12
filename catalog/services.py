from config.settings import CACHE_ENABLED
from .models import Product
from django.core.cache import cache


def get_product_from_cache():
    """Получение данных из кеша, если кеш пустой, то получает данные из базы данных"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product

    product = Product.objects.all()
    cache.set(key, product)
    return product


def get_product_by_category(category_id):
    return Product.objects.filter(category_id=category_id)
