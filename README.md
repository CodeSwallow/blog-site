# Blog Site
General Blog Site


## Example Post Content for Post Model:

# Appium Tests with Robot Framework
Uses the library robotframework and robotframework_appiumlibrary <br>

## Table of Contents
[TOC]
# [First Header of Content](#first-header-of-content)
# [Second Header of Content](#second-header-of-content)
# [Another Header with more Stuff](#another-header-with-more-stuff)
# [Header with different sections inside](#header-with-different-sections-inside)
## [Section 1](#section-1)
## [Section 2](#section-2)
## [Section 3](#section-3)
# [Last Header](#last-header)


## First Header of Content
This is a paragraph within the header. <br>

## Second Header of Content
Here I'm showing a command
```
python -m pip install django
```

## Another Header with more Stuff
A snippet of python code showing a django generic ListView:

```python
from django.views import generic

from blogs.models import Post


class HomePageView(generic.ListView):
    queryset = Post.objects.all().order_by('-pub_date')
    template_name = 'blogs/homepage.html'
    paginate_by = 10
```

This is another snippet of code showing json:
```json
{
  "username": "user_1",
  "password": "user_password_123"
}
```

## Header with different sections inside:
There are different sections here
### Section 1
This is section 1
This is how you register the models in the admin page:
```python
from django.contrib import admin
from blogs.models import (
    Post,
    Category,
    Series
)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Series)
```
### Section 2
This is section 2
### Section 3
This is section 3

## Last Header
<h1>Last Header</h1> <br>
Will come up with different elements to test the markdown language later
```python
from django.views import generic

from blogs.models import Post


class HomePageView(generic.ListView):
    queryset = Post.objects.all().order_by('-pub_date')
    template_name = 'blogs/homepage.html'
    paginate_by = 10
```
