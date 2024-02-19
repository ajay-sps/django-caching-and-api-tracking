from rest_framework import serializers
from bookTracking.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')


class BookNestedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')

    def create(self, validated_data):
        author_details = validated_data.pop('author')
        print(author_details)
        author_instance = Author.objects.create(**author_details)
        book = Book.objects.create(author = author_instance,**validated_data)
        return book