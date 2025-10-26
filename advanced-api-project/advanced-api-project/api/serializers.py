from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

#BookSerializer serializes all Book fields and ensures publication_year isn't in the future.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

#AuthorSerializer serializes Author fields and includes nested BookSerializer for related books.
# This provides a complete view of an author along with their books.

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']