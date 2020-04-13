from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('new/', views.MovieCreateView.as_view(), name='movie_create'),
    path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
]
