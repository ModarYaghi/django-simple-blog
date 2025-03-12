# from django.shortcuts import get_object_or_404, render
from django.views.generic import (  # to switch to generic class-based views
    DetailView,
    ListView,
)

from .models import Post

# Create your views here.
#


# def post_list_view(request):
#     posts = Post.objects.all()  # type: ignore
#     return render(request, "home.html", {"posts": posts})
#


class BlogListView(ListView):
    model = Post  # the Post model we want to view as list
    template_name = "home.html"  # the template will present this view.
    #
    # unnecessary, but it makes thigs esier to understand.
    context_object_name = "posts"


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     return render(request, "post_detail.html", {"post": post})


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    #
    # unnecessary, but it makes things esier to understand.
    contex_object_name = "post"
