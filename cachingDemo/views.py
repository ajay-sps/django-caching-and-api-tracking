from django.shortcuts import render
from rest_framework.views import APIView
from cachingDemo.models import Products
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views import View
from django.utils.decorators import method_decorator
from django.core.cache import cache
from rest_framework.response import Response
from cachingDemo.mixins import TrackRequestsMixin
from django.core.serializers import serialize


@cache_page(60 * 15)
def get_products(request):

    start_time = timezone.now()
    products = Products.objects.all()
    response = render(request,'products.html',{'products':products})
    end_time = timezone.now()
    elapsed_time  = end_time - start_time
    response['elapsed_time'] = elapsed_time.total_seconds()
    response['testing'] = 'testing'
    print(elapsed_time.total_seconds())
    return response 

class HomeView(TrackRequestsMixin, APIView):

    @method_decorator(cache_page(60 * 3))
    def get(self,request):
        print(1111)
        start_time = timezone.now()
        products = cache.get('tota_products')
        if products is None:
            print('hello')
            products = Products.objects.all()
            cache.set('tota_products',products, timeout=360)
        response = render(request,'products.html',{'products':products})
        end_time = timezone.now()
        elapsed_time  = end_time - start_time
        response['elapsed_time'] = elapsed_time.total_seconds()
        response['testing'] = 'testing'
        print(elapsed_time.total_seconds())
        return response


class ProductsView(TrackRequestsMixin, APIView):
    def get(self,requset):
        products = Products.objects.all()
        serialized_data = serialize('json',products)
        return Response({'products':serialized_data})