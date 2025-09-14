from django.shortcuts import render
from .models import Book, Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context