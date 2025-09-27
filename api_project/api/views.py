from django.shortcuts import render
from django.views import View
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets, permissions


# Create your views here.
class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permissions_classes = [permissions.IsAuthenticated] # a logged in user can access




