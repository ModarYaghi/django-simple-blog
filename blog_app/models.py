from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):  # type: ignore
        return self.title

    def get_absolute_url(self):
        # on a CreatView, the following will redirect to 'post_detail'
        # after save/submit new CreateView
        return reverse("post_detail", kwargs={"pk": self.pk})
