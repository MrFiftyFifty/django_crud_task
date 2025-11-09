from django.urls import path
from . import views

urlpatterns = [
    # Book URLs (HTML-based)
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/new/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:book_id>/', views.BookDetailUpdateDeleteView.as_view(), name='book_detail'),
    path('books/<int:book_id>/edit/', views.BookEditView.as_view(), name='book_edit'),
    
    # Author URLs (JSON API)
    path('authors/', views.AuthorListCreateView.as_view(), name='author_list_create'),
    path('authors/<int:author_id>/', views.AuthorDetailView.as_view(), name='author_detail'),
]
