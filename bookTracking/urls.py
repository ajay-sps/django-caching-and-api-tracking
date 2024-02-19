from django.urls import path
from bookTracking.views import BooksView


urlpatterns = [
    path('',BooksView.as_view(),name='books_view'),
    path('update/<int:id>',BooksView.as_view(),name="update_book"),
    path('delete/<int:id>',BooksView.as_view(),name="delete_book"),
]