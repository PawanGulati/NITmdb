from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
]
