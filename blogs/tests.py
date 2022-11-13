from django.test import TestCase

from blogs.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create()

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/post/1')
