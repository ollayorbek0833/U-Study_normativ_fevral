from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from books.forms import BookForm
from books.models import Book
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    ordering = ["created_at"]


class BookCreateView(CreateView):
    model = Book
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books:list")
    form_class = BookForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mode"] = "create"
        return ctx


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books:list")
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mode"] = "update"
        return ctx
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url =  reverse_lazy("books:list")
    context_object_name = 'book'