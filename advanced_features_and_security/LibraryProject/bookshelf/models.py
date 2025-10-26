from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    
class CustomUserManager(models.Model):
    
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password)

objects = CustomUserManager()

def __str__(self):
    return self.username
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view", "Can view article"),
            ("can_create", "Can create article"),
            ("can_edit", "Can edit article"),
            ("can_delete", "Can delete article"),
        ]

    def __str__(self):
        return self.title

    