from django.contrib import admin

# Register your models here.
from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('Book')
    search_fields = ('Book')