from django.contrib import admin
from blogs.models import (
    Post,
    Category,
    Series
)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Series)
