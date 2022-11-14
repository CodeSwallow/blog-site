from django.views import generic
from django.db.models import Q

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


class SearchResultsView(generic.ListView):
    model = Post
    template_name = "blogs/search_results.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("search")
        post_list = Post.objects.filter(
            Q(title__contains=query) | Q(categories__title__contains=query)
        ).distinct()
        return post_list
