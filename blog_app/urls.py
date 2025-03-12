# blog/urls.py
from django.urls import path

from .views import post_detail_view, post_list_view

urlpatterns = [
    path("post/<int:pk>/", post_detail_view, name="post_detail"),
    path("", post_list_view, name="home"),
]
