from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
    , CommentCreateView, CommentUpdateView, CommentDeleteView
)
from .views import search_posts, posts_by_tag

urlpatterns = [
    # Post CRUD URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),          # Create
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),     # Read
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),# Update
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),# Delete

    # Comment URLs
    path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Tag and Search URLs
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts-by-tag'),
]
