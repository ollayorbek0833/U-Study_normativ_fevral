from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login

from books.forms import BookForm, LoginForm, RegisterForm
from books.models import Book, Post
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


def post_list(request):
    q = request.GET.get("q","").strip()

    queryset = Post.objects.order_by("-created_at")
    if q:
        queryset = queryset.filter(
            Q(title__icontains=q) | Q(content__icontains=q)
        )
    
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "posts":page_obj,
        "page_obj":page_obj,
        "q":q,
    }
    return render(request, "books/post_list.html", context)


def register_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "books/register.html", {"form":form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            return redirect("post-list")
    else:
        form = LoginForm()
    
    return render(request, "books/login.html", {"form":form})