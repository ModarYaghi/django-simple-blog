# blog/urls.py
from django.urls import path

# from .views import post_detail_view, post_list_view
from .views import BlogDetailView, BlogListView  # import the generic clas-based views

urlpatterns = [
    # path("post/<int:pk>/", post_detail_view, name="post_detail"),
    #
    # this is how to build url for generic class-based view
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    #
    # path("", post_list_view, name="home"),
    path("", BlogListView.as_view(), name="home"),
]
