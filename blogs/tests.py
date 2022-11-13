from django.test import TestCase
from django.contrib.auth import get_user_model

from blogs.models import (
    Post,
    Category,
    Series
)


def create_user(email='user@example.com', password='test_pass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)


class PostModelTest(TestCase):
    """Test for post model."""

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='Django Blog',
            slug='django-blog',
            overview='Create a django blog',
            content='Content of django blog tutorial',
            table_of_contents='table...',
            author=create_user()
        )

    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'Django Blog')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/post/django-blog')


class CategoryModelTest(TestCase):
    """Test for post category model."""

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            title='django',
            slug='django'
        )

    def test_object_name_is_title(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'django')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/category/django')


class SeriesModelTest(TestCase):
    """Test for post series model."""

    @classmethod
    def setUpTestData(cls):
        Series.objects.create(
            title='Django Blog Series',
            slug='django-blog-series'
        )

    def test_object_name_is_title(self):
        series = Series.objects.get(id=1)
        self.assertEqual(str(series), 'Django Blog Series')

    def test_get_absolute_url(self):
        series = Series.objects.get(id=1)
        self.assertEqual(series.get_absolute_url(), '/series/django-blog-series')
