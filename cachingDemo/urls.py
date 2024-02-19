from django.urls import path
from cachingDemo.views import HomeView,get_products, ProductsView


urlpatterns = [
    path('products',HomeView.as_view()),
    path('productsData',ProductsView.as_view())
]