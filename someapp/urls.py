from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
]