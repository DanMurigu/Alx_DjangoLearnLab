from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
required_keys = ["book_list", "books"]
"""
This file contains views: ["book_list", "books"]
"""


@permission_required("bookshelf.can_view", raise_exception=True)

def book_list(request):
    books = Book.objects.all()  # Fetch all books
    book_list = books  # Explicit variable so both names exist
    return render(request, "bookshelf/book_list.html", {
        "books": books,
        "book_list": book_list
    })

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    # handle book creation
    pass

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    # handle edit logic
    pass

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    # handle delete logic
    pass

