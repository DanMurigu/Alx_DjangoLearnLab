from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('Book')
    search_fields = ('Book')
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("phone_number", "date_of_birth", "profile_picture", "bio"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("phone_number", "date_of_birth", "profile_picture", "bio"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)