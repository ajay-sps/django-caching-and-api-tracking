from django.contrib import admin
from cachingDemo.models import Products
from django.core.cache import caches


admin.site.register(Products)
# admin.site.register(caches['default'].cache_model)
