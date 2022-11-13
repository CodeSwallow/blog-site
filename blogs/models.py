from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Series(models.Model):
    """Post series including various posts"""
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), unique=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular series instance."""
        return reverse("series-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Post(models.Model):
    """Model for blog posts."""
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), unique=True)
    overview = models.TextField(_("overview"))
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
    content = models.TextField(_("content"))
    table_of_contents = models.TextField(_("table of contents"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    featured = models.BooleanField(_("featured"), default=False)
    pub_date = models.DateTimeField(_('publish date'), default=timezone.now)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular post instance."""
        return reverse("post-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    """Blog category."""
    title = models.CharField(_("title"), max_length=20)
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        """Returns the URL to access a particular category instance."""
        return reverse("category-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
