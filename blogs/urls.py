from django.urls import path

from blogs import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('series/', views.SeriesListView.as_view(), name='series-list'),
    path('series/<slug:slug>', views.SeriesDetailView.as_view(), name='series-detail'),
    path('categories/', views.CategoryListView.as_view(), name='list'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
]