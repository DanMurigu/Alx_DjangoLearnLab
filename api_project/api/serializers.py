from rest_framework import serializers
from .models import Book #imports the book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # includes all fields in the Book model
    