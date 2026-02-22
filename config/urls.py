from django.contrib import admin
from django.urls import include, path

from books.views import post_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", include("books.urls")),
    path("posts/", post_list, name="post-list"),
]
