# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Thanks to related_name="librarian"
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Example usage
if __name__ == "__main__":
    # Replace with actual names that exist in your DB
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    for book in get_books_by_author(author_name):
        print(f"- {book.title}")

    print(f"\nBooks in {library_name}:")
    for book in get_books_in_library(library_name):
        print(f"- {book.title}")

    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"\nThe librarian of {library_name} is {librarian.name}")
    else:
        print(f"\nNo librarian found for {library_name}")
