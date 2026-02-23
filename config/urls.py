from django.contrib import admin
from django.urls import include, path

from books.views import login_view, post_list, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", include("books.urls")),
    path("posts/", post_list, name="post-list"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
]
