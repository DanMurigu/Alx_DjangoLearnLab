from django.urls import path
from . import views
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('books/list/', BookListView.as_view(), name='book_list_view'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
    path('books/create/', BookCreateView.as_view(), name='book_create_view'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update_view'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete_view'),
]