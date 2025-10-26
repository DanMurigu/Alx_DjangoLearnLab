from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article
from .models import Book
from .forms import ExampleForm

# Create your views here.


@permission_required('your_app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

@permission_required('your_app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'articles/article_form.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect('article_list')
    return render(request, 'articles/article_form.html', {'article': article})

@permission_required('your_app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

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
