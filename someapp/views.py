from django.shortcuts import render
from django.views.generic import View
from .models import Author, Book

class MyListView(View):
    model = None
    template_name = None
    context_object_name = 'object_list'
    
    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self):
        queryset = self.get_queryset()
        return {
            self.context_object_name: queryset
        }
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class AuthorListView(MyListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'
    
    def get_queryset(self):
        return self.model.objects.filter(full_name__startswith='А')



class BookListView(MyListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class MyDetailView(View):
    model = None
    template_name = None
    context_object_name = 'object'
    
    def get_object(self, pk):
        return self.model.objects.get(pk=pk)
    
    def get_context_data(self, pk):
        obj = self.get_object(pk)
        return {self.context_object_name: obj}
    
    def get(self, request, pk):
        context = self.get_context_data(pk)
        return render(request, self.template_name, context)


class AuthorDetailView(MyDetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'
    
    def get_context_data(self, pk):
        author = self.get_object(pk)
        books = author.books.all()
        
        return {
            'author': author,
            'books': books  
        }


class BookDetailView(MyDetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'