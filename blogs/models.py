from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    """Model for blog posts"""

    def get_absolute_url(self):
        """Returns the URL to access a particular user instance."""
        return reverse('post-detail', args=[str(self.id)])
