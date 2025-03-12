from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
#
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(  # type: ignore
            title="A test title",
            body="This is test body",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A test title")
        self.assertEqual(self.post.body, "This is test body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A test title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)  # type: ignore

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)  # type: ignore

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)  # type: ignore
        self.assertContains(response, "This is test body")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)  # type: ignore
        self.assertEqual(no_response.status_code, 404)  # type: ignore
        self.assertContains(response, "A test title")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_createview(self):
        response = self.client.post(
            reverse("new_post"),
            {
                "title": "New title",  # new post title test
                "body": "New text",  # New post text  test
                "author": self.user.id,  # new author test
            },
        )
        self.assertEqual(response.status_code, 302)  # type: ignore
        self.assertEqual(Post.objects.last().title, "New title")  # type: ignore
        self.assertEqual(Post.objects.last().body, "New text")  # type: ignore

    def test_post_updateview(self):
        response = self.client.post(
            reverse("edit_post", args="1"),
            {
                "title": "Updated title",  # updete post title test
                "body": "Updated text",  # update post body test
            },
        )
        self.assertEqual(response.status_code, 302)  # type: ignore
        self.assertEqual(Post.objects.last().title, "Updated title")  # type: ignore
        self.assertEqual(Post.objects.last().body, "Updated text")  # type: ignore

    def test_post_deleteview(self):
        response = self.client.post(reverse("delete_post", args="1"))
        self.assertEqual(response.status_code, 302)  # type: ignore
