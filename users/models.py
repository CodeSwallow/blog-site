from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    """Custom user for easier modification."""

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

