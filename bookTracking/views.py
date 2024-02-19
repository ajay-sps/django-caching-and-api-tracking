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
from bookTracking.serializers import BookNestedSerializer
from bookTracking.models import Book
from rest_framework import status


class BooksView(TrackRequestsMixin, APIView):
    
    def get(self, request):
        books = Book.objects.all()
        serializer = BookNestedSerializer(books,many= True)
        return render(request,'booksManagement.html',{'books':serializer.data})

    def post(self, request):
        try:
            data = request.data
            serializer = BookNestedSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'book':serializer.data})
            else:
                return Response({'error':serializer.errors})
        except Exception as e:
            return Response({'error':str(e)})

        
    def put(self, request, id):
        try:
            data = request.data
            try:
                book = Book.objects.get(id = id)
            except Book.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = BookNestedSerializer(book,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'book':serializer.data})
            else:
                return Response({'error':serializer.errors})
        except Exception as e:
            return Response({'error':str(e)})
        
    def delete(self, request, id):
        try:
            book = Book.objects.get(id = id)
            book.delete()
            return Response({'message':'Book deleted successfully'})
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


