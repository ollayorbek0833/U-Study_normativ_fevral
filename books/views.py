from django.shortcuts import get_object_or_404, redirect, render

from books.forms import BookForm
from books.models import Book


# Create your views here.


def book_list (request):
    books = Book.objects.all().order_by("-created_at")
    return render(request, "books/book_list.html", {"books": books})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books:list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form, "mode": "create"})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect("books:list")
    else:
        form = BookForm(instance = book)
        return render(request, "books/book_form.html", {"form": form, "mode": "update"})
    

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("books:list")
    return render(request, "books/book_confirm_delete.html", {"book": book})