from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.
#


def post_list_view(request):
    posts = Post.objects.all()  # type: ignore
    return render(request, "home.html", {"posts": posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, "post_detail.html", {"post": post})
