from django.urls import path

from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post'),
    path('series/', views.SeriesListView.as_view(), name='series-list'),
    path('series/<slug:slug>', views.SeriesDetailView.as_view(), name='series-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
]
