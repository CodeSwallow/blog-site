from django.views import generic

from blogs.models import (
    Post,
    Series,
    Category
)


class HomePageView(generic.ListView):
    queryset = Post.objects.all().order_by('-pub_date')
    template_name = 'blogs/homepage.html'
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post


class SeriesListView(generic.ListView):
    model = Series
    paginate_by = 10


class SeriesDetailView(generic.DetailView):
    model = Series


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 10


class CategoryDetailView(generic.DetailView):
    model = Category
