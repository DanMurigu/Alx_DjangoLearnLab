from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    search_posts, posts_by_tag
)

urlpatterns = [
    # Post CRUD URLs (singular)
    path('post/', PostListView.as_view(), name='post-list'),                  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),          # Create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   # Read
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),# Delete

    # Comment URLs
    path('post/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Tag and Search URLs
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts-by-tag'),
]
