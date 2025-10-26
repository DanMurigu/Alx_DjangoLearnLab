from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
# Returns a list of all authors with their nested books
@api_view(['GET'])
def author_list(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

# Returns a list of all books
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)